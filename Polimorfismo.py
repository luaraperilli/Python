# Nome: Luara Perilli
# Matrícula: 2022004841

from abc import ABC, abstractmethod


class EmpDomestica(ABC):

  def __init__(self, nome, telefone):
    self.__nome = nome
    self.__telefone = telefone

  @property
  def nome(self):
    return self.__nome

  @property
  def telefone(self):
    return self.__telefone

  # método abstrato definido na superclasse
  @abstractmethod
  def calculaSalario(self):
    pass


class Horista(EmpDomestica):

  def __init__(self, nome, telefone, horasTrabalhadas, valorPorHora):
    super().__init__(nome, telefone)
    self.__horasTrabalhadas = horasTrabalhadas
    self.__valorPorHora = valorPorHora

  @property
  def horasTrabalhadas(self):
    return self.__horasTrabalhadas

  @property
  def valorPorHora(self):
    return self.__valorPorHora

  # setter
  @valorPorHora.setter
  def valorPorHora(self, valorPorHora):
    self.__valorPorHora = valorPorHora

  def calculaSalario(self):
    return self.valorPorHora * self.horasTrabalhadas


class Diarista(EmpDomestica):

  def __init__(self, nome, telefone, diasTrabalhados, valorPorDia):
    super().__init__(nome, telefone)
    self.__diasTrabalhados = diasTrabalhados
    self.__valorPorDia = valorPorDia

  @property
  def diasTrabalhados(self):
    return self.__diasTrabalhados

  @property
  def valorPorDia(self):
    return self.__valorPorDia

  # setter
  @valorPorDia.setter
  def valorPorDia(self, valorPorDia):
    self.__valorPorDia = valorPorDia

  def calculaSalario(self):
    return self.valorPorDia * self.diasTrabalhados


class Mensalista(EmpDomestica):

  def __init__(self, nome, telefone, valorMensal):
    super().__init__(nome, telefone)
    self.__valorMensal = valorMensal

  @property
  def valorMensal(self):
    return self.__valorMensal

  @valorMensal.setter
  def valorMensal(self, valorMensal):
    self.__valorMensal = valorMensal

  def calculaSalario(self):
    return self.__valorMensal


if __name__ == "__main__":
  emp1 = Horista("Marcela", "(35)9999-9999", 160, 12)
  emp2 = Diarista("Lúcia", "(22)9999-9999", 20, 65)
  emp3 = Mensalista("Valéria", "(11)9999-9999", 1200)

  emp1.valorPorHora = 12
  emp3.valorMensal = 1200

  # adiciona as empregadas na lista
  emps = [emp1, emp2, emp3]

  # define a melhor empregada como sendo a primeira
  melhorEmpregada = emp1

  for emp in emps:
    if emp.calculaSalario() < melhorEmpregada.calculaSalario():
      melhorEmpregada = emp
    print('Nome: ', emp.nome)
    print('Telefone: ', emp.telefone)
    print('Salário: ', emp.calculaSalario())
    print()

print("Melhor Empregada: ", melhorEmpregada.nome)
print("Telefone: ", melhorEmpregada.telefone)
print("Salário: ", melhorEmpregada.calculaSalario())
