from dataclasses import dataclass

@dataclass
class Pessoa:
    _nome:str
    _sobrenome:str
 
    @property
    def nome(self):
        return self._nome
    
    @property
    def sobrenome(self):
        return self._sobrenome

    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    

if __name__=='__main__':

    p1=Pessoa('Neto' ,'show')
    p2=Pessoa('Neto' ,'top')
    
    print(p2.nome_completo)

    print('')
    p2.nome='Iderval'
    p2._sobrenome='Neto'
    print('')

    print(p1.nome_completo)
    print(p2.nome_completo)
