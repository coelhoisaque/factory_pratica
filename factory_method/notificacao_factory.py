from abc import ABC, abstractmethod
from notificacao import Notificacao



class NotificacaoFactory(ABC):
    """Factory Method abstrato para criar objetos de pagamento."""
    @abstractmethod
    def criarNotificacao(self) -> Notificacao:
        """Factory Method: cada subclasse implementa sua própria lógica de criação"""
        pass
   
# Concrete Creator - Factory Method Pattern
class EmailFactory(NotificacaoFactory):
    """Factory concreta para criar notificações por email."""
    
    def criarNotificacao(self) -> Notificacao:
        """Factory Method: cria uma instância de Email"""
        
        return Email()  
    
class SMSFactory(NotificacaoFactory):
    """Factory concreta para criar notificações por SMS."""
    
    def criarNotificacao(self) -> Notificacao:
        """Factory Method: cria uma instância de SMS"""
        from sms import SMS
        return SMS()

class WhatsappFactory(NotificacaoFactory):
    """Factory concreta para criar notificações por WhatsApp."""
    
    def criarNotificacao(self) -> Notificacao:
        """Factory Method: cria uma instância de WhatsApp"""
        from whatsapp import Whatsapp
        return Whatsapp()