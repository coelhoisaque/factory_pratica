from pagamento import Pagamento

# Produto concreto
class Boleto(Pagamento):
    def pagar(self) -> str:
        return "Pago com boleto!"