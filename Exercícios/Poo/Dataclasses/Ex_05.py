#asdict converte a classe apra um ducionario
#astuple converte a classe apra uma tupla

from dataclasses import dataclass, asdict,astuple

@dataclass
class Pessoa():
    nome:str
    idade:int
    def __init_subclass__(self,nome:str,idade:int)->None:
        self.nome=nome
        self.idade=idade

if __name__== '__main__':

    p1=Pessoa('Neto' ,22)
    p2=Pessoa('Neto' ,22)

    print(asdict(p1).keys())
    print(asdict(p1).values())
    print(asdict(p1).items())
    print(astuple(p1)[0])
  