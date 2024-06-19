import random
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from TicTacToe import TicTacToe

class IgracAgent(Agent):
    class PlayBehaviour(CyclicBehaviour):
        async def run(self):
            game = self.agent.game
            if game.current_winner or not game.empty_squares():
                print(f"Game over! Pobjednik: {game.current_winner}")
                await self.agent.stop()
                return

            self.agent.referee_agent = 'agent3@localhost'

            if game.num_empty_squares() % 2 == (0 if self.agent.letter == 'X' else 1):
                if self.agent.strategy == 'random':
                    move = random.choice(game.available_moves())
                elif self.agent.strategy == 'minmax':
                    if game.num_empty_squares() == 9 and self.agent.letter == 'O':
                        move = random.choice(game.available_moves())
                    else:
                        move = game.minimax(game.board, self.agent.letter)['position']

                game.make_move(move, self.agent.letter)
                print("\nTrenutno stanje ploče:")
                game.print_board()

                msg = Message(to=self.agent.referee_agent)
                msg.body = str(move)
                print(f"{self.agent.letter} šalje potez {move} sucu")
                await self.send(msg)

                if game.current_winner:
                    print(f"Igrac {self.agent.letter} je pobijedio!")
                    await self.agent.stop()
                    return

            else:
                print(f"{self.agent.letter} čeka na potez")
                msg = await self.receive(timeout=10)
                if msg:
                    move = int(msg.body)
                    print(f"{self.agent.letter} je primio potez {move} od suca")
                    game.make_move(move, 'O' if self.agent.letter == 'X' else 'X')
                    print("Trenutno stanje ploče:")
                    game.print_board()
                else:
                    print(f"Nije primljen potez od {self.agent.letter}, kraj igre.")
                    await self.agent.stop()

    async def setup(self):
        self.game = TicTacToe()
        self.letter = 'X' if 'agent1' in self.jid else 'O'
        self.strategy = getattr(self, 'strategy', 'random')
        b = self.PlayBehaviour()
        template = Template()
        self.add_behaviour(b, template)