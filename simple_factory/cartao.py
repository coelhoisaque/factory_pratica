from pagamento import Pagamento

# Produto concreto
class Cartao(Pagamento):
    def pagar(self) -> str:
        return "Pagamento realizado com cartão de crédito/débito!"