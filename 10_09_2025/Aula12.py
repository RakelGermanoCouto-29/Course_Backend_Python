''' Métodos de encapsulamento 

__init__() __str__()

-> __init__()
    é chamado automaticamente quando um objeto é criado a partir de uma classe. Sua função é inicializar
    os atrivutos do objeto com valores iniciais.
    EX: 
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto("Caneta", 2.5)
print(p1.nome)  # Saída: Caneta
print(p1.preco) # Saída: 2.5

o parâmetro self refere-se á própria instância do objetos, é executado uma única vez na criação 
do objeto e pode receber parâmetros para inicializar atributos. 

-> __str__()
    Retorna uma representação em string do objeto quando:
        usamos a função print() ou str() em um objeto.
    Sem o método __str()__, o print() mostra apenas a referência de memória do objeto.

    EX:
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: {self.preco}"

p1 = Produto("Notebook", 3500.00)
print(p1)

---------------------------------------------------------------------------------------------------


O que é encapsulamento?

é o conceito de esconder detalhes de implementação e proteger os dados de um objeto.

Permite controlar o acesso aos atributos de uma classe, definindo quais podem ser 
acessados diretamente e quais devem ser acessados através de métodos.

TIPO       CONVENÇÃO      ACESSO
Público     self.nome    Acessível de qualquer lugar
Protegido    self._nome   Acessível dentro da classe e suas subclasses
Privado     self.__nome   Acessível apenas dentro da classe

Getters e Setters

Métodos que permitem acessar (get) e modificar (set) atributos privados ou protegidos de forma controlada.

Ex:
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular  # Atributo público
        self.__saldo = saldo      # Atributo privado

    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("Saldo não pode ser negativo")

conta = Conta("Rakel", 1000)
print(conta.get_saldo())  # Acessa o saldo através do getter

conta.set_saldo(1500)     # Modifica o saldo através do setter
print(conta.get_saldo())  # Saída: 1500

conta.set_saldo(-500)     # Tenta definir um saldo negativo
print(conta.get_saldo())  # Saída: 1500 (saldo não foi alterado) '''

# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular  # Atributo público
#         self.__saldo = saldo      # Atributo privado

#     def get_saldo(self):
#         return self.__saldo
    
#     def set_saldo(self, valor):
#         if valor >= 0:
#             self.__saldo = valor
#         else:
#             print("Saldo não pode ser negativo")

# conta = Conta("Rakel", 1000)
# print(conta.get_saldo())  # Acessa o saldo através do getter

# conta.set_saldo(1500)     # Modifica o saldo através do setter
# print(conta.get_saldo())  # Saída: 1500

# conta.set_saldo(-500)     # Tenta definir um saldo negativo
# print(conta.get_saldo())  # Saída: 1500 (saldo não foi alterado)

# print(conta.titular)    # Acessa o atributo público diretamente

#---------------- Atividade 01 ---------------

'''Criar uma classe FUNCIONÁRIO com os seguintes requisitos:
Atributos:
  nome
  salario
Métodos:
    __str__()
    Encapsular salário (atributo privado)
Usar Getter e Setter para acessar e modificar o salário.'''


# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.__salario = salario

#     def __str__(self):
#         return f"Funcionário: {self.nome}, Salário: {self.__salario}"
    
#     def get_salario(self):
#         return self.__salario

#     def set_salario(self, valor):
#         if valor >= 0:
#             self.__salario = valor
#         else:
#             print("Salário não pode ser negativo")



# ListaFuncionarios = []

# def mostrar_funcionarios():
#     print("\nLista de Funcionários:")
#     for funcionario in ListaFuncionarios:
#         print(funcionario)

# i = int(input("Quantos funcionários deseja cadastrar?"))

# for a in range(i):
#     nome = str(input(f"Digite o nome do {a+1}° funcionário: "))
#     salario = float(input(f"Digite o salário do funcionário de nome {nome}: "))
#     funcionario = Funcionario(nome, salario)
#     ListaFuncionarios.append(funcionario)

# mostrar_funcionarios()

# print ("\nAtualizar o salário dos funcionários:\n")

# for funcionario in ListaFuncionarios:
#     novo_salario = float(input(f"Digite o novo salário para {funcionario.nome}: "))
#     funcionario.set_salario(novo_salario)
    
# mostrar_funcionarios()


# #---------------- Atividade 02 ---------------
# '''Criar uma classe ContaBancaria com os seguintes requisitos:
# Atributo privado: saldo
# Métodos para depósito e saque com validação
# Método para consultar saldo'''

# class ContaBancaria:
#     def __init__(self, saldo_inicial = 0):
#         self.__saldo = saldo_inicial
    
#     def deposito(self, valor):
#         if valor > 0 :
#             self.__saldo += valor 
#             print("Valor depositado.")
#         else:
#             print("Digite um valor positivo maior que 0.")
    
#     def sacar(self, valor):
#         if valor > 0 :
#             if valor > self.__saldo:
#                 print("Saldo insuficiente!! Vá trabalhar.")
#             else:
#                 self.__saldo -= valor
#                 print("Valor sacado.")
#         else:
#             print("Digite um valor positivo maior que 0.")

#     def __str__(self):
#         return f"Seu saldo é {self.__saldo}"

#     # def consulta(self):
#     #     return self.__saldo

# minha_conta = ContaBancaria()

# while True:
#     comando = int(input("Bem vindo ao seu banco. Digite 1 para depositar, 2 para sacar, 3 para consultar o saldo ou 4 para sair."))
    
#     match comando:
#         case 1:
#             ValorDepositado = int(input("Digite o valor a ser depositado: "))
#             minha_conta.deposito(ValorDepositado)
            
        
#         case 2:
#             valor = int(input("Digite o valor a ser sacado: "))
#             minha_conta.sacar(valor) 
        
#         case 3: 
#             print(minha_conta)
#             # print(f"Seu saldo é: {minha_conta.consulta()}")
            
        
#         case 4: 
#             break

# ---------------- Atividade 03 ----------------
'''Criar uma classe Cliente com atributos públicos e privados. Implementar métodos de acesso e exibição 
Atributos:
    nome (público)
    email (público)
    __cpf (privado)
    __saldo (privado)
'''

# class Cliente:
#     def __init__(self, nome, email, cpf, saldo_inicial=0):
#         self.nome = nome
#         self.email = email
#         self.__cpf = cpf
#         self.__saldo = saldo_inicial

#     def adicionar_saldo(self, valor):
#         if valor > 0:
#             self.__saldo += valor 
#             print("✅ Valor depositado com sucesso!")
#         else:
#             print("⚠️ Digite um valor positivo maior que 0.")
    
#     def exibir_saldo(self):
#         print(f"💰 Saldo atual: R$ {self.__saldo:.2f}")
    
#     def exibir_cpf(self):
#         print(f"🔐 CPF do cliente: {self.__cpf}")
    
#     def __str__(self):
#         return (
#             f"📄 Dados do Cliente\n"
#             f"Nome: {self.nome}\n"
#             f"Email: {self.email}\n"
#             f"CPF: {self.__cpf}\n"
#             f"Saldo: R$ {self.__saldo:.2f}"
#         )

# # Função para mostrar o menu
# def exibir_menu():
#     print("\n===== MENU DO BANCO =====")
#     print("1 - 📝 Cadastrar cliente")
#     print("2 - 💵 Adicionar saldo")
#     print("3 - 📈 Consultar saldo")
#     print("4 - 🔍 Consultar CPF")
#     print("5 - 📄 Consultar dados do cliente")
#     print("6 - ❌ Sair")

# # Programa principal
# def main():
#     meu_cliente = None
    
#     while True:
#         exibir_menu()
#         try:
#             comando = int(input("Escolha uma opção: "))
#         except ValueError:
#             print("⚠️ Entrada inválida. Digite um número de 1 a 6.")
#             continue

#         if comando == 1:
#             nome = input("Informe o nome do cliente: ").strip()
#             email = input("Informe o email do cliente: ").strip()
#             cpf = input("Informe o CPF do cliente: ").strip()
#             meu_cliente = Cliente(nome, email, cpf)
#             print("✅ Cliente cadastrado com sucesso!")

#         elif comando in [2, 3, 4, 5]:
#             if not meu_cliente:
#                 print("⚠️ Você precisa cadastrar o cliente primeiro (opção 1).")
#                 continue

#             if comando == 2:
#                 try:
#                     valor = float(input("Digite o valor a ser adicionado: R$ "))
#                     meu_cliente.adicionar_saldo(valor)
#                 except ValueError:
#                     print("⚠️ Entrada inválida. Digite um número válido.")
#             elif comando == 3:
#                 meu_cliente.exibir_saldo()
#             elif comando == 4:
#                 meu_cliente.exibir_cpf()
#             elif comando == 5:
#                 print(meu_cliente)

#         elif comando == 6:
#             print("👋 Encerrando o sistema. Obrigado por usar nosso banco!")
#             break

#         else:
#             print("⚠️ Opção inválida. Escolha uma opção de 1 a 6.")

# # Executar o programa
# if __name__ == "__main__":
#     main()


# ---------------- Atividade 04 ----------------
'''Criar uma classe Produto com atributos privados e métodos para aplicar desconto (com validação).

    __nome
    __preco
    __estoque 
    
'''

class Produto:
    def __init__(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque
    
    def aplicar_desconto(self, desconto):
        if 0 < desconto < 100:
            desconto = desconto/100
            self.__preco -= self.__preco * desconto
        else:
            print("⚠️ Digite um valor entre 0 e 100.")
    
    def __str__(self):
        return (
            f"📄 Dados do Produto\n"
            f"Produto: {self.__nome}\n"
            f"Preço: {self.__preco}\n"
            f"Estoque: {self.__estoque} un"
        )

def exibir_menu():
    print("\n===== CADASTRO DE PRODUTO =====")
    print("1 - 📝 Cadastrar Produto")
    print("2 - 💵 Adicionar desconto")
    print("3 - 📄 Consultar dados")
    print("4 - ❌ Sair")
meu_produto = ""

while True:
    
    exibir_menu()
    try:
        comando = int(input("Escolha uma opção: "))
    except ValueError:
        print("⚠️ Entrada inválida. Digite um número de 1 a 4.")
        continue

    match comando:
        case 1:
            nome = input("Informe o nome do produto: ").strip()
            preco = float(input("Informe o preço do produto: ").strip())
            estoque = input("Informe a quantidade produto: ").strip()
            
            meu_produto = Produto(nome, preco, estoque)
            print("✅ Produto cadastrado com sucesso!")

        case 2:
            if not meu_produto:
                print("⚠️ Você precisa cadastrar o produto primeiro (opção 1).")
                continue
            elif comando == 2:
                try:
                    desconto = float(input("Digite o desconto a ser aplicado: "))
                    meu_produto.aplicar_desconto(desconto)
                except ValueError:
                    print("⚠️ Entrada inválida. Digite um número válido.")
        case 3:
            if not meu_produto:
                print("⚠️ Você precisa cadastrar o produto primeiro (opção 1).")
                continue
            elif comando == 3:
                print(meu_produto)
        
        case 4:
            print("👋 Encerrando o sistema. Obrigado!")
            break




