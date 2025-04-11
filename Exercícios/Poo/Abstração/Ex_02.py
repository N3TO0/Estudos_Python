from abc import ABC, abstractmethod

class Porta(ABC):
    def __init__(self,nome):
        self.nome=nome
    
    @abstractmethod
    def abrir(self):
        pass

    @abstractmethod
    def fechar(self):
        pass

class PortaCarro(Porta):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f'{self.nome} abriu!')
    
    def fechar(self):
        print(f'{self.nome} fechou!')

class PortaQuarto(Porta):
    def __init__(self, nome):
        super().__init__(nome)

    def abrir(self):
        print(f'{self.nome} abriu!')
    
    def fechar(self):
        print(f'{self.nome} fechou!')

class PortaCofre(Porta):

    def __init__(self, nome):
        super().__init__(nome)
    
    def abrir(self):
        print(f'{self.nome} abriu!')

    def fechar(self):
        print(f'{self.nome} fechou!')
        


p1=PortaCarro('Porta do carro')
p2=PortaQuarto('Porta do quarto')
p3=PortaCofre("Porta do cofre")

p1.abrir()
p1.fechar()

p2.abrir()
p2.fechar()

p3.abrir()
p3.fechar()
