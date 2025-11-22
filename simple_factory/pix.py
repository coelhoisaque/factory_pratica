from pagamento import Pagamento

# Produto concreto
class Pix(Pagamento):
    def pagar(self) -> str:
        return "Pago com pix!"