from dataclasses import dataclass, field

@dataclass
class Pessoa:
    
    nome:str ='Neto'
    idade:int ='Show'
    idade: int = 0
    endereco: list[str] = field(default_factory=list)
    

if __name__=='__main__':
    p1=Pessoa()
    p2=Pessoa()

    print(p1.nome)
    print(p1.idade)
    print(p1 == p2)