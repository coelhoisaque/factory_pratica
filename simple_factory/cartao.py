from pagamento import Pagamento

# Produto concreto
class Cartao(Pagamento):
    def pagar(self) -> str:
        return "Pago com cartão!"