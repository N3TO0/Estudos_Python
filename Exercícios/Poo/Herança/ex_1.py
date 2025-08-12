# herança simples

class Veiculo():
    def __init__ (self, placa, ano, modelo, tipo):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.tipo = tipo

    def ficha(self):
        print(f"placa: {self.placa}\nano: {self.ano}\nmodelo: {self.modelo}\ntipo: {self.tipo}\n")

class Moto(Veiculo):
    def __init__ (self, placa, ano, modelo):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.tipo = "moto"

class Carro(Veiculo):
    def __init__ (self, placa, ano, modelo):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.tipo = "carro"

class Caminhao(Veiculo):
    def __init__ (self, placa, ano, modelo):
        self.placa = placa
        self.ano = ano
        self.modelo = modelo
        self.tipo = "caminhao"

transporte1=Moto(22934, 2011, "fz25")

transporte1.ficha()