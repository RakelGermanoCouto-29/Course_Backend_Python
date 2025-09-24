class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.__salario = salario

    def __str__(self):
        return f"Funcionário: {self.nome}, Salário: {self.__salario}"
    
    def get_salario(self):
        return self.__salario

    def set_salario(self, valor):
        if valor >= 0:
            self.__salario = valor
        else:
            print("Salário não pode ser negativo")



ListaFuncionarios = []

def mostrar_funcionarios():
    print("\nLista de Funcionários:")
    for funcionario in ListaFuncionarios:
        print(funcionario)

i = int(input("Quantos funcionários deseja cadastrar?"))

for a in range(i):
    nome = str(input(f"Digite o nome do {a+1}° funcionário: "))
    salario = float(input(f"Digite o salário do funcionário de nome {nome}: "))
    funcionario = Funcionario(nome, salario)
    ListaFuncionarios.append(funcionario)

mostrar_funcionarios()

print ("\nAtualizando salários...\n")

for funcionario in ListaFuncionarios:
    novo_salario = float(input(f"Digite o novo salário para {funcionario.nome}: "))
    funcionario.set_salario(novo_salario)
    
mostrar_funcionarios()