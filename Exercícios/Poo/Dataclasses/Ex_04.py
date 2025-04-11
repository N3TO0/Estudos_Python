#init=False desativa o initi, assim tendo que criar um init

from dataclasses import dataclass

@dataclass
class Pessoa(init=False):
    nome:str
    idade:int
    def __init_subclass__(self,nome:str,idade:int)->None:
        self.nome=nome
        self.idade=idade

if __name__== '__main__':
    
    p1=Pessoa('Neto' ,22)
    p2=Pessoa('Neto' ,22)

    print(p1.nome)
    print(p1.idade)
    print(p1 == p2)