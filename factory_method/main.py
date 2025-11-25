from pagamento_factory import CartaoFactory
from pagamento_factory import PixFactory
from pagamento_factory import BoletoFactory

# Uso do Factory Method pattern 
if __name__ == "__main__":
    

    print("=== SISTEMA DE PAGAMENTO (Factory Method) ===\n")

    # Cada factory concreta cria seu próprio tipo de pagamento
    cartao_factory = CartaoFactory()
    
    # Usar a fábrica para criar um pagamento por cartão
    pagamento_cartao = cartao_factory.criarPagamento()
    print(pagamento_cartao.pagar()) # saída: Pagamento realizado com cartão de crédito/débito!

    # Exemplo adicional: criar pagamento por PIX
    pix_factory = PixFactory()
    pagamento_pix = pix_factory.criarPagamento()
    print(pagamento_pix.pagar())  # saída: Pagamento realizado via PIX!

    # Exemplo adicional: criar pagamento por Boleto
    boleto_factory = BoletoFactory()
    pagamento_boleto = boleto_factory.criarPagamento()
    print(pagamento_boleto.pagar())  # saída: Pagamento realizado via Boleto!