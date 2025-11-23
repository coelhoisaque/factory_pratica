from notificacao import Notificacao

# Produto concreto
class SMS(Notificacao):
    def enviar(self) -> str:
        return "SMS de notificação enviado!"