from email import Email

# Factory Method: classe responsável por criar notificações
class NotificacaoFactory:
    """Simple Factory para criar objetos de Notificação."""
    
    @staticmethod
    def criarNotificacao(tipo: str):
        """Cria notificações baseado no tipo."""
        if tipo == "email":
            return Email()
        else:
            raise ValueError(f"Tipo de notificação não conhecido: {tipo}")