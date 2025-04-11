#Metodo de classe ( @classmethod )

class Pessoa:
    ano=2023

    def __init__(self,nome,idade):
        self.nome=nome
        self.idade=idade

    def metodo_de_classe(self):
        print('hey')

    @classmethod
    def adiciona_50(cls,idade):
        return cls('anonima',50)

p1=Pessoa('neto',21)
print(Pessoa.ano)
Pessoa.metodo_de_classe(p1) 

p2= Pessoa.adiciona_50('Helena ')
print(p2.nome,p2.idade)

p3=Pessoa('anonima', 34)
print(p3.nome,p3.idade)



