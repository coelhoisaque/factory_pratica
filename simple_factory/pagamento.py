from abc import ABC, abstractmethod

# Interface / produto
class Pagamento(ABC):
    @abstractmethod
    def pagar(self) -> str:
        pass