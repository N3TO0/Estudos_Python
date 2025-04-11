#Encapsulamento (modificadores de acesso: public, _protected, __ private)

#public: pode ser acessada em qualquer local Ex: .

#protected:  não deve ser usado fora da classe ou subclasses Ex: ._

#Private:  só deve ser usado na classe em que foi declarado Ex: .__

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

#-----------------------------------------------------------

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade= idade

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self,valor):
        if valor < 0:
            raise ValueError('Não é possivel')
        self._idade = valor
        
p1=Pessoa('neto', 22)

print(p1.nome,p1.idade)
try:
    p1.idade = -2
except ValueError as e:
    print(e)

print(p1.nome,p1.idade)