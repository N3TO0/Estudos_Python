import Pessoas 
import Contas 

class Banco:
    def __init__(self, agencias: list[int] | None = None, clientes: list[Pessoas.Pessoa] | None = None):
        self.agencias = agencias or []
        self.clientes = clientes or []

    def autenticar(self, cliente=None, conta=None):
        if conta:  # Verifica se uma conta foi passada
            return conta.agencia in self.agencias
        elif cliente:  # Verifica se um cliente foi passado
            return cliente.conta.agencia in self.agencias if cliente.conta else False
        return False  # Caso nenhum argumento seja passado

if __name__ == '__main__':
    p1 = Pessoas.Cliente('iderval', 18)
    cc1 = Contas.ContaCorrente(111, 222, 500)
    p1.conta = cc1  # Associar a conta ao cliente

    p2 = Pessoas.Cliente('Neto', 22)
    cc2 = Contas.ContaCorrente(131, 332, 100)
    p2.conta = cc2  # Associar a conta ao cliente

    banco = Banco()
    banco.clientes.extend([p1, p2])  # Adiciona apenas os clientes
    banco.agencias.extend([111, 222, 131])  # Adiciona as agências

    # Agora você pode autenticar a conta
    print(banco.autenticar(conta=cc1))  # Verifica a autenticação da conta
    # Ou, se você quiser autenticar o cliente
    print(banco.autenticar(cliente=p1))  # Verifica a autenticação do cliente
            
