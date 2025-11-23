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
   
def demonstrarNotificacoes():
    notificacao_email = NotificacaoFactory.criarNotificacao("email")
    print(notificacao_email.enviar())

    notificacao_sms = NotificacaoFactory.criarNotificacao("sms")
    print(notificacao_sms.enviar())

    notificacao_whatsapp = NotificacaoFactory.criarNotificacao("whatsapp")
    print(notificacao_whatsapp.enviar())

if __name__ == "__main__":
    demonstrarPaganentos()
    demonstrarNotificacoes()


   