class Vendedor:
    def __init__ (self, nome):
        self.nome = nome
        self.vendas = 0
        self.meta = 50
    def vendeu(self, vendas):
        self.vendas=vendas

    def bateu_meta(self,):
        if self.vendas > self.meta:
            print(f'{self.nome} bateu a meta')
        else:
            print(f'{self.nome} não bateu a meta')

vendedor1= Vendedor('Neto')
vendedor2= Vendedor('Tomas')
vendedor3= Vendedor('Lucas')

vendedor1.vendeu(530)
vendedor1.bateu_meta()

vendedor2.vendeu(11)
vendedor2.bateu_meta()

vendedor3.vendeu(46)
vendedor3.bateu_meta()
