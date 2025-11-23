from pagamento import Pagamento

# Produto concreto
class Cartao(Pagamento):
    def pagar(self) -> str:
        """Retorna a confirmação da geração do pagamento por cartão."""
        return "Pagamento realizado com cartão de crédito/débito!"