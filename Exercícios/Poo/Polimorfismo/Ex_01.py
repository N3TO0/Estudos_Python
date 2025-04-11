#polimorfismo, assinatura do metodo e 
#liskov substitution penciple

#obs: Assinatura é o metodo, os parametros, a ordem dos parametros, o "retorno"

from abc import ABC, abstractmethod

class Notificacao(ABC):

    def __init__(self,mensagem):
        self.mensagem = mensagem
    
    @abstractmethod
    def enviar(self) -> bool: pass

class NotificacaoEmail(Notificacao):

    def enviar(self) -> bool: 
        print('Email: enviando:',self.mensagem)
        return True

class NotificacaoSms(Notificacao):

    def enviar(self) -> bool: 
        print('SMS: enviando:',self.mensagem)
        return False

def notifica(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()
    
    if notificacao_enviada:
        print('notificação enviada')
    else:
        print('Notificação não enviada')

n=NotificacaoSms('testando notificação 1')
b=NotificacaoEmail('testando notificação 2')

notifica(n)
notifica(b)

