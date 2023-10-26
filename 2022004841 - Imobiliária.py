# Luara Perilli
# 2022004841

from abc import ABC, abstractmethod


class Vendedor(ABC):
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__vendas = []
    
    @property
    def codigo(self):
        return self.__codigo 

    @property
    def nome(self):
        return self.__nome

    @property
    def vendas(self):
        return self.__vendas

    def adicionaVenda(self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__vendas.append(Venda(codImovel, mesVenda, anoVenda, valorVenda))

    @abstractmethod
    def getDados(self):
        pass

    @abstractmethod
    def calculaRenda(self, mesVenda, anoVenda):
        pass
    
class Venda():
    def __init__(self, codImovel, mesVenda, anoVenda, valorVenda):
        self.__codImovel = codImovel
        self.__mesVenda = mesVenda
        self.__anoVenda = anoVenda
        self.__valorVenda = valorVenda
        
    @property
    def codImovel(self):
        return self.__codImovel
    
    @property
    def mesVenda(self):
        return self.__mesVenda
    
    @property
    def anoVenda(self):
        return self.__anoVenda
    
    @property
    def valorVenda(self):
        return self.__valorVenda
    
class Contratado(Vendedor):
    def __init__(self, codigo, nome, salarioFixo, nroCartTrabalho):
        super().__init__(codigo, nome)
        self.__salarioFixo = salarioFixo 
        self.__nroCartTrabalho = nroCartTrabalho
        
    @property
    def salarioFixo(self):
        return self.__salarioFixo

    @property
    def nroCartTrabalho(self):
        return self.__nroCartTrabalho
        
    def getDados(self):
        return f"Nome: {self.nome} - Nro Carteira:  {self.nroCartTrabalho}"

    def calculaRenda(self, mes, ano):
        salario = self.salarioFixo
        for venda in self.vendas:
            if venda.mesVenda == mes and venda.anoVenda == ano:
                salario += venda.valorVenda * 1 / 100
        return salario
    
class Comissionado(Vendedor):
    def __init__(self, codigo, nome, nroCPF, comissao):
        super().__init__(codigo, nome)
        self.__nroCPF = nroCPF
        self.__comissao = comissao
        
    @property
    def nroCPF(self):
        return self.__nroCPF
    
    @property
    def comissao(self):
        return self.__comissao
    
    def getDados(self):
        return f"Nome: {self.nome} - Nro CPF: {self.nroCPF}"

    def calculaRenda(self, mes, ano):
        salario = 0
        for venda in self.vendas: 
            if venda.mesVenda == mes and venda.anoVenda == ano:
                salario += venda.valorVenda * self.comissao/100
        return salario
    
if __name__ == "__main__":
    funcContratado = Contratado(1001, "João da Silva", 2000, 1234)
    
    funcContratado.adicionaVenda(100, 3, 2022, 200000)
    funcContratado.adicionaVenda(101, 3, 2022, 300000)
    funcContratado.adicionaVenda(102, 4, 2022, 600000)
    
    funcComissionado = Comissionado(1002, "José Santos", 4321, 5)
    
    funcComissionado.adicionaVenda(200, 3, 2022, 200000)
    funcComissionado.adicionaVenda(201, 3, 2022, 400000)
    funcComissionado.adicionaVenda(202, 4, 2022, 500000)
    
    listaFunc = [funcContratado, funcComissionado]
    
    for func in listaFunc:
        print(func.getDados())
        print("Renda no mês 3 de 2022: ")
        print(func.calculaRenda(3, 2022))
        
        