from pagamento_factory import PagamentoFactory
from notificacao_factory import NotificacaoFactory

# Uso
def demonstrarPaganentos():
    pagamento_cartao = PagamentoFactory.criarPagamentoOnline("cartão")
    print(pagamento_cartao.pagar()) 

    # pagamento1 = PagamentoFactory.criarPagamento("pix")
    # print(pagamento1.pagar()) 

    # pagamento1 = PagamentoFactory.criarPagamento("boleto")
    # print(pagamento1.pagar()) 

    # notificao1 = NotificacaoFactory.criarNotificacao("email")
    # print(notificao1.enviar())

if __name__ == "__main__":
    demonstrarPaganentos()


   