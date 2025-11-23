from pagamento import Pagamento
from cartao import Cartao
from pix import Pix
from boleto import Boleto

# Factory Method: classe responsável por criar pagamentos
class PagamentoFactory:
    """Simple Factory para criar objetos de pagamento."""
    
    @staticmethod
    def criarPagamentoOnline(pagamentoType: str) -> Pagamento:
        """Cria pagamentos online (cartão ou PIX)."""
        if pagamentoType == "cartão":
            return Cartao()
        elif pagamentoType == "pix":
            return Pix()
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoType}")
        
    @staticmethod
    def criarPagamentoOffline(pagamentoType: str) -> Pagamento:
        """Cria  pagamentos offline."""
        if pagamentoType == "boleto":
            return Boleto()
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoType}")