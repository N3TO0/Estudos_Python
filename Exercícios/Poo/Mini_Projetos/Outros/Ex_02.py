#class Carro:
#    def __init__(self, nome, motor, fabricante):
#        self.nome=nome
#        self.motor=motor
#        self.fabricante=fabricante

#    @property
#    def retorno(self):
#        print(f'{self.fabricante.nome} é fabricante da {self.nome} que tem o motor {self.motor.nome}')
    
#class Motor:
#    def __init__(self,nome):
#        self.nome=nome

#class Fabricante:
#    def __init__(self,nome):
#        self.nome=nome

#c1=Carro('Fiat',Motor('0800'), Fabricante('Tomas'))
#c1.retorno

#------------------------------------------------------
class Carro:
    def __init__(self, nome):
        self.nome=nome
        self._motor= None
        self._fabricante=None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,valor):
        self._motor =valor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante =valor
    
    
    def retorno(self):
        print(f'{self.nome} tem o motor {self.motor.nome} e o fabricante é {self.fabricante.nome}')

class   Motor:
    def __init__(self, nome):
        self.nome=nome

class Fabricante:
    def __init__(self, nome):
        self.nome=nome

carro1=Carro('Gol')
fabricante=Fabricante('Tonny')
motor=Motor('0800')
carro1.fabricante = fabricante
carro1.motor = motor

carro1.retorno()
#-----------------------------
carro2=Carro('uno')
fabricante=Fabricante('Neto')
motor=Motor('1800')
carro2.fabricante = fabricante
carro2.motor = motor

carro2.retorno()
 