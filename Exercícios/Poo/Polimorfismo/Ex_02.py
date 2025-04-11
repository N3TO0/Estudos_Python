from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    @abstractmethod
    def calcular_salario(self):
        pass

class FuncionarioAnalista(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 0.1* self.salario_base # bonus de 10%

class FuncionarioGerente(Funcionario):
    def __init__(self, nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.salario_base + self.bonus

class FuncionarioEstagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base # Estagiario não recebe bonus

def exibir_salario(funcionario):                  #Função para retornar o retorno de cada 
    return funcionario.calcular_salario()         #metodo "calcular _salario"da classe que o objeto pertencer !

analista1 = FuncionarioAnalista(nome="Ana", salario_base=5000)
gerente1 = FuncionarioGerente(nome="Carlos", salario_base=8000, bonus=2000)
estagiario1 = FuncionarioEstagiario(nome="Eduardo", salario_base=2000)

print(f"salario de {analista1.nome}: R${exibir_salario(analista1):,.2f}")
print(f"salario de {gerente1.nome}: R${exibir_salario(gerente1):,.2f}")
print(f"salario de {estagiario1.nome}: R${exibir_salario(estagiario1):,.2f}")