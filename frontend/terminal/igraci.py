import re

from tic_tac_toe.igra.igraci import Player
from tic_tac_toe.logika.iznimke import InvalidMove
from tic_tac_toe.logika.modeli import GameState, Move

class ConsolePlayer(Player):
    def get_move(self, game_state: GameState) -> Move | None:
        while not game_state.game_over:
            try:
                index = grid_to_index(input(f"{self.mark} je na redu: ").strip())
            except ValueError:
                print("Unesite odabrano polje u obliku A1 ili 1A")
            else:
                try:
                    return game_state.make_move_to(index)
                except InvalidMove:
                    print("Polje je već popunjeno!")
        return None

def grid_to_index(grid: str) -> int:
    if re.match(r"[abcABC][123]", grid):
        col, row = grid
    elif re.match(r"[123][abcABC]", grid):
        row, col = grid
    else:
        raise ValueError("Krive koordinate polja")
    return 3 * (int(row) - 1) + (ord(col.upper()) - ord("A"))
