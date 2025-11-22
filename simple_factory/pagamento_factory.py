from pagamento import Pagamento
from cartao import Cartao
from pix import Pix
from boleto import Boleto

# Factory Method: classe responsável por criar pagamentos
class PagamentoFactory:
    @staticmethod
    def criarPagamento(pagamentoType: str) -> Pagamento:
        if pagamentoType == "cartão":
            return Cartao()
        elif pagamentoType == "pix":
            return Pix()
        elif pagamentoType == "boleto":
            return Boleto()
        else:
            raise ValueError(f"Tipo de pagamento não conhecido: {pagamentoType}")