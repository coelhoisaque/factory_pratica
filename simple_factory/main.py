from pagamento_factory import PagamentoFactory

# Uso
if __name__ == "__main__":
    pagamento1 = PagamentoFactory.criarPagamento("cartão")
    print(pagamento1.pagar()) 

    pagamento1 = PagamentoFactory.criarPagamento("pix")
    print(pagamento1.pagar()) 

    pagamento1 = PagamentoFactory.criarPagamento("boleto")
    print(pagamento1.pagar()) 

   