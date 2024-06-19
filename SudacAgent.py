from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template
from TicTacToe import TicTacToe

class SudacAgent(Agent):
    class GameBehaviour(CyclicBehaviour):
        async def run(self):
            game = self.agent.game
            while not game.current_winner and game.empty_squares():
                """
                if game.num_empty_squares() == 3:
                    print("Ostala su 3 prazna polja i nema pobjednika. Igra zavrsava nerijeseno")
                    break
                """   
                if game.num_empty_squares() % 2 == 0:
                    current_player = 'agent1@localhost'
                    player_letter = 'X'
                else:
                    current_player = 'agent2@localhost'
                    player_letter = 'O'

                print(f"Sudac čeka na potez od {player_letter}")
                msg = await self.receive(timeout=10)
                if msg:
                    move = int(msg.body)
                    letter = 'X' if current_player == 'agent1@localhost' else 'O'
                    if game.make_move(move, letter):
                        print(f"Sudac: Potez {move} od {letter} je valjan!")
                        game.print_board()
                        if game.current_winner:
                            print(f"Igrac {letter} je pobijedio!")
                        elif not game.empty_squares():
                            print("Neriješeno!")

                    next_player = 'agent2@localhost' if current_player == 'agent1@localhost' else 'agent1@localhost'
                    msg = Message(to=next_player)
                    msg.body = str(move)
                    await self.send(msg)
                else:
                    print(f"Nije primljen potez od {player_letter}, kraj igre.")
                    break

            await self.agent.stop()

    async def setup(self):
        self.game = TicTacToe()
        b = self.GameBehaviour()
        template = Template()
        self.add_behaviour(b, template)