from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia:int ,conta:int ,saldo:float=0) -> None:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self,valor:float) -> float:
        ...

    def depositar(self,valor:float) -> float:
        self.saldo += valor
        self.Verificar(f'(Deposito: R${valor:.2f})')
        return self.saldo
    
    def Verificar(self,msg:str ='') -> None:
        print(f'Saldo: R${self.saldo:.2f} {msg}')

class ContaPoupanca(Conta):

    def sacar(self,valor: float):
        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >=0:
            self.saldo -= valor
            self.Verificar(f'(Saque R${valor:.2f})')
            return self.saldo
        
        print('\nNão foi possivel sacar o valor desejado')
        self.Verificar(f'(Saque Negado de R${valor:.2f})\n')
        return self.saldo
    
class ContaCorrente(Conta):

    def __init__(self, agencia:int, conta:int, saldo:float=0, limite:float =100) : #acrescentando um atributo
        super().__init__(agencia, conta, saldo)
        self.limite=limite

    def sacar(self,valor:float): #função sacar
        valor_pos_saque = self.saldo - valor #efinindo o valor pos saque
        valor_max = -self.limite
        
        
        if valor_pos_saque >= valor_max:
            self.saldo -= valor
            self.Verificar(f'(Saque R${valor:.2f})')
            return self.saldo
        
        print('\nNão foi possivel sacar o valor desejado, valor passou do limite!')
        self.Verificar(f'(Saque Negado de R${valor:.2f})')
        print(f'Limite:R$ {valor_max:.2f}\n')
        return self.saldo
    

if __name__ == '__main__':
    
    conta1=ContaPoupanca(111,222)
    conta1.depositar(500)
    conta1.sacar(500)
    conta1.sacar(5)

    print('-'*40)

    conta2=ContaCorrente(111,222)
    conta2.depositar(500)
    conta2.sacar(599)
    conta2.sacar(1)
    conta2.sacar(5)
     