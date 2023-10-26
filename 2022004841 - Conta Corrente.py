from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__ (self, numConta, nomeCorrentista, saldo):
        self._numConta = numConta
        self._nomeCorrentista = nomeCorrentista
        self._saldo = saldo
        self._transacoes = []
        
    @property
    def numConta(self):
        return self._numConta 
    
    @property
    def nomeCorrentista(self):
        return self._nomeCorrentista
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def transacoes(self):
        return self._transacoes
    
    # métodos abstratos definidos na superclasse
    @abstractmethod
    def ImprimirExtrato(self):
        pass
    
    @abstractmethod
    def Deposito(self, valor, descricao):
        pass
            
    @abstractmethod
    def Retirada(self, valor, descricao):
        pass
        
class ContaCorrenteComum(Conta):
    def __init__(self, numConta, nomeCorrentista, saldo):
        super().__init__(numConta, nomeCorrentista, saldo)
   
    def ImprimirExtrato(self):
        print("Conta Corrente Comum")
        print("Número da Conta:", self.numConta)
        print("Nome do Correntista:", self.nomeCorrentista)
        
        for descricao, valor in self.transacoes:
           print("{}: R${:.2f}".format(descricao, valor))
        print("Saldo: R${:.2f}".format(self.saldo))
        
    def Deposito(self, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._transacoes.append((descricao, valor))
        else: 
            print("Valor do depósito inválido")
        
    def Retirada(self, valor, descricao):
        if self.saldo >= valor:
            self._saldo -= valor
            self._transacoes.append((descricao, -valor))
        else:
            print("Saldo insuficiente para retirada") 
    
class ContaCorrenteComLimite(Conta):
    def __init__(self, numConta, nomeCorrentista, saldo, valorDoLimite):
        super().__init__(numConta, nomeCorrentista, saldo)
        self._valorDoLimite = valorDoLimite
        
    @property
    def valorDoLimite(self):
        return self._valorDoLimite
    
    def ImprimirExtrato(self):
        print("Conta com Limite")
        print("Número da Conta:", self.numConta)
        print("Nome do Correntista:", self.nomeCorrentista)
        for descricao, valor in self.transacoes:
            print("{}: R${:.2f}".format(descricao, valor))
        print("Saldo: R${:.2f}".format(self.saldo))
        print("Limite: R${:.2f}".format(self.valorDoLimite))

    def Deposito(self, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._transacoes.append((descricao, valor))
        else: 
            print("Valor do depósito inválido")

    def Retirada(self, valor, descricao):
        if self.saldo + self.valorDoLimite >= valor:
            self._saldo -= valor
            self._transacoes.append((descricao, -valor))
        else:
            print("Limite de saldo excedido para retirada")
    
class ContaPoupança(Conta):
    def __init__(self, numConta, nomeCorrentista, saldo, aniversarioConta):
        super().__init__(numConta, nomeCorrentista, saldo)
        self._aniversarioConta = aniversarioConta
        
    @property
    def aniversarioConta(self):
        return self._aniversarioConta
    
    def ImprimirExtrato(self):
        print("Conta Poupança")
        print("Número da Conta:", self.numConta)
        print("Nome do Correntista:", self.nomeCorrentista)
        for descricao, valor in self.transacoes:
           print("{}: R${:.2f}".format(descricao, valor))
        print("Saldo: R${:.2f}".format(self.saldo))
    
    def Deposito(self, valor, descricao):
        if valor > 0:
            self._saldo += valor
            self._transacoes.append((descricao, valor))
        else: 
            print("Valor do depósito inválido")
        
    def Retirada(self, valor, descricao):
        if self.saldo >= valor:
            self._saldo -= valor
            self._transacoes.append((descricao, -valor))
        else:
            print("Saldo insuficiente para retirada") 
            
# Teste
if __name__ == "__main__":
    conta_comum = ContaCorrenteComum(1, "Mariana", 1000)
    conta_limite = ContaCorrenteComLimite(2, "Maria", 500, 1000)
    conta_poupanca = ContaPoupança(3, "Miguel", 2000, "01/10") 
    
    conta_comum.Deposito(200, "Depósito")
    conta_limite.Deposito(300, "Depósito")
    conta_poupanca.Deposito(400, "Depósito")
    
    conta_comum.Retirada(300, "Retirada")
    conta_limite.Retirada(800, "Retirada")
    conta_poupanca.Retirada(150, "Retirada")
    
    contas = [conta_comum, conta_limite, conta_poupanca]

    for conta in contas:
        conta.ImprimirExtrato()
        print("\n")
