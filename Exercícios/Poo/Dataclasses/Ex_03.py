#frosen=tue congela a classe

from dataclasses import dataclass

@dataclass
class Pessoa(frozen=True):
    nome:str
    idade:int

if __name__=='__main__':
    p1=Pessoa('Neto' ,22)
    p2=Pessoa('Neto' ,22)

    print(p1.nome)
    print(p1.idade)
    print(p1 == p2)