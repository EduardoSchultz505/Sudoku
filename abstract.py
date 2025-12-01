from abc import ABC, abstractmethod
from tabuleiro import Board

class JogoBase(ABC):
    """Abstração por contrato."""

    @abstractmethod
    def inicio(self):
        pass

    @abstractmethod
    def jogar(self, board: Board):
        pass
