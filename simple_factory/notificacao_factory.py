from email import Email
from sms import SMS
from whatsapp import Whatsapp

# Factory Method: classe responsável por criar notificações
class NotificacaoFactory:
    """Simple Factory para criar objetos de Notificação."""
    
    @staticmethod
    def criarNotificacao(tipo: str):
        """Cria notificações baseado no tipo."""
        if tipo == "email":
            return Email()
        elif tipo == "sms":
            return SMS()
        elif tipo ==  "whatsapp":
            return Whatsapp()
        else:
            raise ValueError(f"Tipo de notificação não conhecido: {tipo}")