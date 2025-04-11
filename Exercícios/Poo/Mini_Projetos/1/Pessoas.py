from abc import ABC, abstractmethod
import Contas

class Pessoa(ABC):
    def __init__(self,nome: str ,idade: int) -> None:
        self._nome=nome
        self._idade=idade

    @property
    def nome(self) -> str:
       return self._nome 
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @nome.setter
    def nome(self,valor:str) -> None:
        if len(valor) >=3:
            self._nome =valor
        else:
           raise ValueError('O nome deve conter mais de 2 letras!')

    @idade.setter
    def idade(self,valor:int) -> None:
        if valor >=0:
             self._idade = valor
             return self._idade
        else:
            raise ValueError('Valor não pode ser negativo!')
        
    

class Cliente(Pessoa):
    def __init__(self, nome:str, idade:int) -> None:
        super().__init__(nome,idade)
        self.conta: Contas.Conta | None = None
    

        
if __name__ =='__main__':

    p1=Cliente('iderval', 18)
    p1.conta = Contas.ContaCorrente(111,222,0,0)
    p1.conta.depositar(100)
    p1.conta.sacar(50)

    print("")
    
    p1.nome= 'Neto'
    p1.idade= 22
    print(p1.nome)
    print(p1.idade)