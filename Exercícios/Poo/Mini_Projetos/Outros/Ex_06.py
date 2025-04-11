from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
        self
    #ContaCorrente
    #ContaPoupança
    pass

class Pessoa(ABC):
    def __init__(self,nome,idade):
        self._nome =None
        self._idade= None

    property
    def nome(self):
        return self._nome 
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    pass

class Cliente(Pessoa):
    pass

class Conta(Cliente):
    pass

class Banco(Cliente,Conta):
    #Banco -> cliente
    #Banco -> conta
    pass

