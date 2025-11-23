from notificacao import Notificacao

# Produto concreto
class Whatsapp(Notificacao):
    def enviar(self) -> str:
        return "WhatsApp de notificação enviado!"