from notificacao import Notificacao

# Produto concreto
class Email(Notificacao):
    def enviar(self) -> str:
        return "Email de notificação enviado!"