from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tic_tac_toe.igra.igraci import Player
    from tic_tac_toe.logika.modeli import GameState, Grid, Mark

import re

from tic_tac_toe.logika.iznimke import InvalidGameState

def validate_grid(grid: Grid) -> None:
    if not re.match(r"^[\sXO]{9}$", grid.cells):
        raise ValueError("Mora sadržavati 9 polja od: X, O ili razmak")

def validate_game_state(game_state: GameState) -> None:
    validate_number_of_marks(game_state.grid)
    validate_starting_mark(game_state.grid, game_state.starting_mark)
    validate_winner(
        game_state.grid, game_state.starting_mark, game_state.winner
    )

def validate_number_of_marks(grid: Grid) -> None:
    if abs(grid.x_count - grid.o_count) > 1:
        raise InvalidGameState("Pogrešan broj X i O")

def validate_starting_mark(grid: Grid, starting_mark: Mark) -> None:
    if grid.x_count > grid.o_count:
        if starting_mark != "X":
            raise InvalidGameState("Pogrešna početna oznaka")
    elif grid.o_count > grid.x_count:
        if starting_mark != "O":
            raise InvalidGameState("Pogrešna početna oznaka")

def validate_winner(
    grid: Grid, starting_mark: Mark, winner: Mark | None) -> None:
    if winner == "X":
        if starting_mark == "X":
            if grid.x_count <= grid.o_count:
                raise InvalidGameState("Pogrešan broj X")
        else:
            if grid.x_count != grid.o_count:
                raise InvalidGameState("Pogrešan broj X")
    elif winner == "O":
        if starting_mark == "O":
            if grid.o_count <= grid.x_count:
                raise InvalidGameState("Pogrešan broj O")
        else:
            if grid.o_count != grid.x_count:
                raise InvalidGameState("Pogrešan broj O")

def validate_players(player1: Player, player2: Player) -> None:
    if player1.mark is player2.mark:
        raise ValueError("Igrači moraju koristiti različite znakove")
