"""Pagamento realizado via PIX."""
from pagamento import Pagamento
# Produto concreto
class Pix(Pagamento):
    """Implementa pagamento por PIX."""
    def pagar(self) -> str:
        """Retorna a confirmação da geração do pagamento por PIX."""
        return "Pagamento realizado com PIX!"