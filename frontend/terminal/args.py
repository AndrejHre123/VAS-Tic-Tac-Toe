import argparse
from typing import NamedTuple

from tic_tac_toe.igra.igraci import(
    Player, 
    RandomComputerPlayer,
    MinmaxComputerPlayer
)

from tic_tac_toe.logika.modeli import Mark

from .igraci import ConsolePlayer

PLAYER_CLASSES = {
    "covjek": ConsolePlayer,
    "random": RandomComputerPlayer,
    "minmax": MinmaxComputerPlayer
}

class Args(NamedTuple):
    player1: Player
    player2: Player
    starting_mark: Mark

def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-X",
        dest="igrac_x",
        choices=PLAYER_CLASSES.keys(),
        default="covjek",
    )
    parser.add_argument(
        "-O",
        dest="igrac_o",
        choices=PLAYER_CLASSES.keys(),
        default="minmax",
    )
    parser.add_argument(
        "--starting",
        dest="starting_mark",
        choices=Mark,
        type=Mark,
        default="X",
    )
    args = parser.parse_args()

    player1 = PLAYER_CLASSES[args.igrac_x](Mark("X"))
    player2 = PLAYER_CLASSES[args.igrac_o](Mark("O"))

    if args.starting_mark == "O":
        player1, player2 = player2, player1

    return Args(player1, player2, args.starting_mark)