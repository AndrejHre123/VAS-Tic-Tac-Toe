import abc

from tic_tac_toe.logika.modeli import GameState

class Renderer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def render(self, game_state: GameState) -> None:
        """"""