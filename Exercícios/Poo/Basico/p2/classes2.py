class Clientes:
    def __init__(self,nome,email,plano):
        self.nome=nome
        self.email=email
        self.planos=['Basic','Platinum']
        

    #Verificação de entrada de valor plano contem em planos
        if plano in self.planos:
            self.plano = plano
            print('\nsucesso')
        else:
            raise Exception('\nplano invalido')
        
    #Verificação se mudança de plano contem em planos
    def novo_plano(self, novo_plano):
        if novo_plano in self.planos:
            self.plano=novo_plano
        else:
            raise Exception('plano invalido')
    
    def filmes(self,filme,plano_filme):
        if self.plano == plano_filme:
            print(f'\nAssistir filme {filme}')
        elif self.plano == 'Platinum':
            print(f'\nAssistir filme {filme}')
        elif self.plano == 'Basic' and plano_filme == 'Platinum':
            print(f'\nNão tem o plano necessario para\nassistir {filme}')
        else:
            raise Exception('Plano invalido')
        