class Connection:
    def __init__(self,host='localhost'):
        self.host = host
        self.user=None
        self._password=None

    def set_user(self,user):
        self.user = user

    def set_passuord(self, password):
        self._passuord = password

    def acessar(self):
        a=input('digite o usuario').strip() 
        b=input('digite o senha:').strip()
        if self.user == a:
            if self.passuord ==b:
                print('Bem vindo!')
            else:
                print('senha incorreta!')

        else:
            print('Nome de usuario incorreto!')

c1=Connection()

c1.set_user(user=input('Digite seu usuario:').strip())
c1.set_passuord(password=input('Digite sua senha: ').strip())

c1.acessar()
