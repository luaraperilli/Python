# Luara Perilli
# 2022004841

# Definição das exceptions

class TitulacaoInvalida(Exception):
    pass

class IdadeInvalida(Exception):
    pass

class CursoInvalido(Exception):
    pass

class CPFInvalido(Exception):
    pass

class Pessoa():
    def __init__(self, nome, endereco, idade, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__idade = idade
        self.__cpf = cpf
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def endereco(self):
        return self.__endereco
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def cpf(self):
        return self.__cpf
    
    def printDescricao(self):
        pass
    
class Professor(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, titulacao):
        super().__init__(nome, endereco, idade, cpf)
        self.__titulacao = titulacao
        
    @property
    def titulacao(self):
        return self.__titulacao

    def printDescricao(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Titulação: {self.titulacao}")
        
class Aluno(Pessoa):
    def __init__(self, nome, endereco, idade, cpf, curso):
        super().__init__(nome, endereco, idade, cpf)
        self.__curso = curso
        
    @property
    def curso(self):
        return self.__curso
    
    def printDescricao(self):
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Idade: {self.idade}")
        print(f"CPF: {self.cpf}")
        print(f"Curso: {self.curso}")
    
if __name__ == "__main__":
    
    listaPessoas = []
    
    pessoa1 = Professor("Jane", "Av. BPS", 30, 1234, "Doutor")
    pessoa2 = Professor("Luciana", "Rua Prefeito Tigre Maia", 40, 5678, "Doutor")
    pessoa3 = Professor("Marcos", "Rua Doutor Silvestre Ferraz", 35, 3456, "Mestre")
    pessoa4 = Aluno("Lúcia", "Av. BPS", 20, 6789, "SIN")
    pessoa5 = Aluno("Alan", "Rua Padre Toledo Taques", 24, 2345, "Engenharia de Energia")
    pessoa6 = Aluno("Lavínia", "Rua dos Ipês", 32, 7890, "CCO")
    pessoa7 = Professor("Lucas", "Av. dos Autonomistas", 28, 2468, "Doutor")
    
    listaPessoas.append(pessoa1)
    listaPessoas.append(pessoa2)
    listaPessoas.append(pessoa3)
    listaPessoas.append(pessoa4)
    listaPessoas.append(pessoa5)
    listaPessoas.append(pessoa6)
    listaPessoas.append(pessoa7)
    
    cadastro = {}
    
    for pessoa in listaPessoas:
        try: 
            if type(pessoa) == Professor and pessoa.titulacao != "Doutor":
                raise TitulacaoInvalida
            if type(pessoa) == Professor and pessoa.idade < 30:
                raise IdadeInvalida
            if type(pessoa) == Aluno and pessoa.idade < 18:
                raise IdadeInvalida
            if type(pessoa) == Aluno and pessoa.curso != 'CCO' and pessoa.curso != 'SIN':
                raise CursoInvalido
            if pessoa.cpf in cadastro:
                raise CPFInvalido
        except TitulacaoInvalida:
            print()
            print("Erro! Titulação não permitida para cadastro")
        except IdadeInvalida:
            print()
            print("Erro! Idade não permitida para cadastro")
        except CursoInvalido:
            print()
            print("Erro! Curso não permitido para cadastro")
        except CPFInvalido:
            print()
            print("Erro! CPF já cadastrado")
        else:
            cadastro[pessoa.cpf] = pessoa
            print()
            print("Usuário cadastrado!")
            print()
            pessoa.printDescricao()
