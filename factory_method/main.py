from pagamento_factory import CartaoFactory

# Uso do Factory Method pattern 
if __name__ == "__main__":
    

    print("=== SISTEMA DE PAGAMENTO (Factory Method) ===\n")

    # Cada factory concreta cria seu próprio tipo de pagamento
    cartao_factory = CartaoFactory()
    
    # Usar a fábrica para criar um pagamento por cartão
    pagamento_cartao = cartao_factory.criarPagamento()
    print(pagamento_cartao.pagar()) # saída: Pagamento realizado com cartão de crédito/débito!