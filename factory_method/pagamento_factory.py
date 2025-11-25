from abc import ABC, abstractmethod
from pagamento import Pagamento



class PagamentoFactory(ABC):
    """Factory Method abstrato para criar objetos de pagamento."""
    
    @abstractmethod
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass
   
# Concrete Creator - Factory Method Pattern
class CartaoFactory(PagamentoFactory):
    """Factory concreta para criar pagamentos por cartão."""
    
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cria uma instância de Cartão"""
        return Cartao()