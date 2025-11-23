from abc import ABC, abstractmethod

# Interface / produto
class Notificacao(ABC):
    @abstractmethod
    def enviar(self) -> str:
        pass