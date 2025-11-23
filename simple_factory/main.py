from pagamento_factory import PagamentoFactory
from notificacao_factory import NotificacaoFactory

# Uso
def demonstrarPaganentos():
    pagamento_cartao = PagamentoFactory.criarPagamentoOnline("cartão")
    print(pagamento_cartao.pagar()) 

    pagamento_pix = PagamentoFactory.criarPagamentoOnline("pix")
    print(pagamento_pix.pagar())   
 
    pagamento_boleto = PagamentoFactory.criarPagamentoOffline("boleto")
    print(pagamento_boleto.pagar())
   
if __name__ == "__main__":
    demonstrarPaganentos()


   