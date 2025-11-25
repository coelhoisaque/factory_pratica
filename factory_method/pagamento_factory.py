from abc import ABC, abstractmethod
from pagamento import Pagamento
from cartao import Cartao



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

class PixFactory(PagamentoFactory):
    """Factory concreta para criar pagamentos por PIX."""
    
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cria uma instância de Pix"""
        from pix import Pix
        return Pix()
    
class BoletoFactory(PagamentoFactory):
    """Factory concreta para criar pagamentos por boleto."""
    
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cria uma instância de Boleto"""
        from boleto import Boleto
        return Boleto()