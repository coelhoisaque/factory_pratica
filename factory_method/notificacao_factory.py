from abc import ABC, abstractmethod
from notificacao import Notificacao
from note_email import Email
from sms import SMS
from whatsapp import Whatsapp


class NotificacaoFactory(ABC):
    """Factory Method abstrato para criar objetos de pagamento."""
    @abstractmethod
    def criarNotificacao(self, canal: str) -> Notificacao:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass
   
class notificacaoUrgente(NotificacaoFactory):
    def criarNotificacao(self, canal: str) -> Notificacao:
        """Cria notificações urgentes (SMS ou WhatsApp)."""
        if canal == "sms":
            return SMS()
        elif canal == "whatsapp":
            return Whatsapp()
        else:
            raise ValueError(f"Canal de notificação não conhecido para urgente: {canal}")

class notificacaoNormal(NotificacaoFactory):
    def criarNotificacao(self, canal: str) -> Notificacao:
        """Cria notificações normais (email)."""
        if canal == "email":
            return Email()
        else:
            raise ValueError(f"Canal de notificação não conhecido para normal: {canal}")