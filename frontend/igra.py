from tic_tac_toe.igra.engine import TicTacToe
from tic_tac_toe.igra.igraci import RandomComputerPlayer
from tic_tac_toe.logika.modeli import Mark

from terminal.igraci import ConsolePlayer
from terminal.renderers import ConsoleRenderer

player1 = ConsolePlayer(Mark("X"))
player2 = RandomComputerPlayer(Mark("O"))

TicTacToe(player1, player2, ConsoleRenderer()).play()