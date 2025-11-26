from pagamento_factory import pagamentoOnline, pagamentoOffline
from notificacao_factory import notificacaoUrgente, notificacaoNormal

def demonstrarPagamentos():
    print("=== SISTEMA DE PAGAMENTO (Factory Method Corrigido) ===\n")

    # Factory para pagamentos online
    factory_online = pagamentoOnline()
    
    # Criar pagamento por cartão usando a factory online
    pagamento_cartao = factory_online.criarPagamento("cartão")
    print(f"Cartão: {pagamento_cartao.pagar()}")

    # Criar pagamento por PIX usando a factory online
    pagamento_pix = factory_online.criarPagamento("pix")
    print(f"PIX: {pagamento_pix.pagar()}")

    # Factory para pagamentos offline
    factory_offline = pagamentoOffline()
    
    # Criar pagamento por boleto usando a factory offline
    pagamento_boleto = factory_offline.criarPagamento("boleto")
    print(f"Boleto: {pagamento_boleto.pagar()}")

    print("\n" + "="*50)

def demonstrarNotificacoes():
    print("\n=== SISTEMA DE NOTIFICAÇÕES (Factory Method Corrigido) ===\n")

    # Factory para notificações urgentes
    factory_urgente = notificacaoUrgente()
    
    # Criar notificações urgentes
    notificacao_sms_urgente = factory_urgente.criarNotificacao("sms")
    print(f"SMS Urgente: {notificacao_sms_urgente.enviar()}")

    notificacao_whatsapp_urgente = factory_urgente.criarNotificacao("whatsapp")
    print(f"WhatsApp Urgente: {notificacao_whatsapp_urgente.enviar()}")

    # Factory para notificações normais
    factory_normal = notificacaoNormal()
    
    # Criar notificações normais
    notificacao_email_normal = factory_normal.criarNotificacao("email")
    print(f"Email Normal: {notificacao_email_normal.enviar()}")

    print("\n" + "="*50)

def demonstrarTratamentoErros():
    print("\n=== DEMONSTRAÇÃO DE TRATAMENTO DE ERROS ===\n")
    
    factory_online = pagamentoOnline()
    factory_urgente = notificacaoUrgente()
    
    try:
        # Tentativa de criar tipo de pagamento não suportado
        factory_online.criarPagamento("paypal")
    except ValueError as e:
        print(f"Erro esperado no pagamento: {e}")
    
    try:
        # Tentativa de criar canal não suportado para notificação urgente
        factory_urgente.criarNotificacao("email")
    except ValueError as e:
        print(f"Erro esperado na notificação: {e}")

if __name__ == "__main__":
    demonstrarPagamentos()
    demonstrarNotificacoes()
    demonstrarTratamentoErros()