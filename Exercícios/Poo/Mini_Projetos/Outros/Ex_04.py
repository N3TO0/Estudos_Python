#Codigo usando uma função para retorno caso um dev possa mudar o nome de uma instacia futuramente!
class Caneta:

    def __init__(self,cor):
        self.cor_tinta=cor

    def get_cor(self):
        return self.cor_tinta


caneta=Caneta('Azul')

print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())

#Existe o @property que resumidamente, o chamado não precisa colocar parentases

class Caneta:

    def __init__(self,cor):
        self.cor_tinta=cor

    @property
    def get_cor(self):
        return self.cor_tinta


caneta=Caneta('Azul')

print(caneta.get_cor)
print(caneta.get_cor)
print(caneta.get_cor)
print(caneta.get_cor)
print(caneta.get_cor)
