from pagamento import Pagamento

# Produto concreto
class Pix(Pagamento):
    def pagar(self) -> str:
        return "Pagamento realizado com PIX!"