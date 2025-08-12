#herança unica

class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def exibir_info(self):
        print(f"\nMarca: {self.marca}\nAno: {self.ano}\nPostas: {self.portas}\n")

# Teste
c = Carro("Toyota", 2020, 4)
c.exibir_info()



#herança multipla
class Pessoa:
    def __init__(self, nome):
        print("Pessoa init")
        self.nome = nome
        super().__init__()

class Trabalhador:
    def __init__(self, registro):
        print("Trabalhador init")
        self.registro = registro
        super().__init__()

class Medico(Pessoa, Trabalhador):
    def __init__(self, nome, registro, especialidade):
        print("Medico init")
        super().__init__(nome, registro)
        self.especialidade = especialidade

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nRegistro: {self.registro}\nEspecialidade: {self.especialidade}\n")

# Teste
m = Medico("Dra. Ana", "12345", "Cardiologia")
m.exibir_dados()

# Dica: use print(Medico.__mro__) se quiser entender a ordem de execução
