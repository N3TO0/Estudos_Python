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