from abc import ABC, abstractmethod
from pagamento import Pagamento
from cartao import Cartao
from pix import Pix
from boleto import Boleto



class PagamentoFactory(ABC):
    """Factory Method abstrato para criar objetos de pagamento."""
    
    @abstractmethod
    def criarPagamento(self) -> Pagamento:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass


class pagamentoOnline(PagamentoFactory):
    
    def criarPagamento(self, pagamentoType: str) -> Pagamento:
        """Cria pagamentos online (cartão ou PIX)."""
        if pagamentoType == "cartão":
            return Cartao()
        elif pagamentoType == "pix":
            return Pix()
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoType}")

class pagamentoOffline(PagamentoFactory):   
    
    def criarPagamento(self, pagamentoType: str) -> Pagamento:
        """Cria  pagamentos offline."""
        if pagamentoType == "boleto":
            return Boleto()
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoType}")