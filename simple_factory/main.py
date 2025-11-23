from pagamento_factory import PagamentoFactory
from notificacao_factory import NotificacaoFactory

# Uso
def demonstrarPaganentos():
    """Demonstra o uso do sistema de pagamento com Simple Factory."""
    print("=== SISTEMA DE PAGAMENTO (Simple Factory) ===\n")

    print("\n--- Pagamentos online ---\n")
    pagamento_cartao = PagamentoFactory.criarPagamentoOnline("cartão")
    print(pagamento_cartao.pagar()) 

    pagamento_pix = PagamentoFactory.criarPagamentoOnline("pix")
    print(pagamento_pix.pagar())   
 
    print("\n--- Pagamentos offline ---\n")
    pagamento_boleto = PagamentoFactory.criarPagamentoOffline("boleto")
    print(pagamento_boleto.pagar())
   
def demonstrarNotificacoes():
    """Demonstra o uso do sistema de notificações com Simple Factory."""
    print("\n=== SISTEMA DE NOTIFICAÇÕES (Simple Factory) ===\n")

    print("\n--- Notificações Normais ---\n")
    notificacao_email = NotificacaoFactory.criarNotificacao("email")
    print(notificacao_email.enviar())

    print("\n--- Notificações Urgentes ---\n")
    notificacao_sms = NotificacaoFactory.criarNotificacao("sms")
    print(notificacao_sms.enviar())

    notificacao_whatsapp = NotificacaoFactory.criarNotificacao("whatsapp")
    print(notificacao_whatsapp.enviar())

if __name__ == "__main__":
    demonstrarPaganentos()
    demonstrarNotificacoes()


   