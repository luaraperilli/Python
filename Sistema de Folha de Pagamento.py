# Luara Perilli
# 2022004841

from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, codigo, nome, pontoMensalFunc):
        self.__codigo = codigo
        self.__nome = nome 
        self.__pontoMensalFunc = []
        
    @property 
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def pontoMensalFunc(self):
        return self.__pontoMensalFunc
    
    def adicionaPonto(self, mes, ano, faltas, atrasos):
        self.__pontoMensalFunc.append(PontoFunc(mes, ano, faltas, atrasos))
    
    def lancaFaltas(self, mes, ano, faltas):
        for ponto in self.ficha:
            if ponto.mes == mes and ponto.ano == ano:
                ponto.faltas = faltas
                break
    
    def lancaAtrasos(self, mes, ano, atrasos):
        pass
    
    def imprimeFolha(self, mes, ano):
        print("Código: ", self.__codigo)
        print("Nome: ", self.__nome)
    
    @abstractmethod
    def calculaSalario(self, mes, ano):
        pass
    
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass
    
class PontoFunc():
    def __init__ (self, mes, ano, nroFaltas, nroAtrasos):
        self.__mes = mes
        self.__ano = ano
        self.__nroFaltas = nroFaltas
        self.__nroAtrasos = nroAtrasos
        
    @property
    def mes(self):
        return self.__mes
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def nroFaltas(self):
        return self.__nroFaltas
    
    @property
    def nroAtrasos(self):
        return self.__nroAtrasos
    
    def lancaFaltas(self, nroFaltas):
        pass
    
    def lancaAtrasos(self, nroAtrasos):
        pass
    
class Professor(Funcionario):
    def __init__(self, codigo, nome, pontoMensalFunc, titulacao, salarioHora, nroAulas):
        super().__init__(codigo, nome, pontoMensalFunc)
        self.__titulacao = titulacao 
        self.__salarioHora = salarioHora
        self.__nroAulas = nroAulas
        
    @property
    def titulacao(self):
        return self.__titulacao
    
    @property
    def salarioHora(self):
        return self.__salarioHora
    
    @property
    def nroAulas(self):
        return self.__nroAulas
    
    @abstractmethod
    def calculaSalario(self, mes, ano):
        salarioProf = 0 
        salarioProf = self.__salarioHora * self.__nroAulas - self.__salarioHora * self.__nroFaltas 
        return salarioProf
    
    @abstractmethod
    def calculaBonus(self, mes, ano):
        bonus = 0
        if self.__nroFaltas == 0:
            pass
    
class TecAdmin(Funcionario):
    def __init__(self, codigo, nome, pontoMensalFunc, funcao, salarioMensal):
        super().__init__(codigo, nome, pontoMensalFunc)
        self.__funcao = funcao 
        self.__salarioMensal = salarioMensal
        
    @property
    def funcao(self):
        return self.__funcao
    
    @property
    def salarioMensal(self):
        return self.__salarioMensal
    
    @abstractmethod
    def calculaSalario(self, mes, ano):
        return self.__salarioMensal - ((self.__salarioMensal/30)) * self.__nroFaltas
    
    @abstractmethod
    def calculaBonus(self, mes, ano):
        pass
    
if __name__ == "__main__":
    funcionarios = []
    prof = Professor(1, "Joao", "Doutor", 45.35, 32)
    prof.adicionaPonto(4, 2021, 0, 0)
    prof.lancaFaltas(4, 2021, 2)
    prof.lancaAtrasos(4, 2021, 3)
    funcionarios.append(prof)
    tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
    tec.adicionaPonto(4, 2021, 0, 0)
    tec.lancaFaltas(4, 2021, 3)
    tec.lancaAtrasos(4, 2021, 4)
    funcionarios.append(tec)
    for func in funcionarios:
        func.imprimeFolha(4, 2021)
        print()
