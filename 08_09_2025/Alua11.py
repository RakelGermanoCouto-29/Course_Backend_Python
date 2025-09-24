

'''--------------- Atividade 01 ---------------
 Criar uma classe Carro com os seguintes atributos:
  marca
 - modelo
 - ano
Asicionar um método chamado exibir_dados() que mostra todas as informações do carro:'''

# class Carro:
#     def __init__(self, marca,modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano

#     def exibir_dados(self):
#         print(f"Marca: {self.marca}")
#         print(f"Modelo: {self.modelo}")
#         print(f"Ano: {self.ano}")

# marca = input("Marca do carro:")
# modelo = input("modelo do carro:")
# ano = input("ano do carro:")

# carro = Carro(marca, modelo, ano)
# carro.exibir_dados()

'''--------------- Atividade 02 ---------------
 Criar uma classe Aluno com os seguintes atributos:
  Nome
  nota1
  nota2
Asicionar os seguintes métodos:
 - media()
 situação()'''

# class Aluno:
#     def __init__(self, nome, nota1, nota2):
#         self.nome = nome
#         self.nota1 = nota1
#         self.nota2 = nota2

#     def media(self):
#         return (self.nota1 + self.nota2) / 2
    
#     def situacao(self):
#         media = self.media()
#         if media >= 7:
#             print(f"O aluno {self.nome} está aprovado com média {media:.2f}.")
#             return 1
#         else:
#             print(f"O aluno {self.nome} está reprovado com média {media:.2f}.")
#             return 0

# nome = input("Nome: ")
# nota1 = float(input("Nota 1: "))
# nota2 = float(input("Nota 2: "))

# aluno = Aluno(nome, nota1, nota2)
# aluno.situacao()


'''--------------- Atividade 03 ---------------
Os alunos devem criar classes para representar objetos reais e apresentar a estrutura ao final da aula.

Cada grupo deve escolher um dos seguintes objetos:

1. Produto: com atributos como nome, preço, quantidade
2. Conta Bancária: com atributos como titular, saldo
3. Livro: com atributos como título, autor, ano de publicação
4. outro: á escolha do grupo
'''

# class Produto:
#     def __init__(self, nome, preco, quantidade):
#         self.nome = nome
#         self.preco = preco
#         self.quantidade = quantidade
#         print("-"*20)
#         print(f"Produto: {self.nome}\n Preço: {self.preco}\n Quantidade: {self.quantidade}")

    
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo
#         print("-"*20)
#         print(f"Titular: {self.titular}\n Saldo: {self.saldo}")

# class Livro:
#     def __init__(self, titulo, autor, ano_publicacao):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano_publicacao = ano_publicacao
#         print("-"*20)
#         print(f"Título: {self.titulo}\n Autor: {self.autor}\n Ano de Publicação: {self.ano_publicacao}")    

# class Curso:
#     def __init__(self, nome, duracao, instrutor):
#         self.nome = nome
#         self.duracao = duracao
#         self.instrutor = instrutor
#         print("-"*20)
#         print(f"Curso: {self.nome}\n Duração: {self.duracao}\n Instrutor: {self.instrutor}")


# # Produto

# print("Cadastro de Produto")
# nome = input("Nome: ")
# preco = float(input("Preço: "))
# quantidade = int(input("Quantidade: "))

# produto = Produto(nome, preco, quantidade)

# #Conta Bancária
# print("-"*20)
# print("Cadastro de Conta Bancária")
# titular = input("Titular: ")
# saldo = float(input("Saldo: ")) 

# conta = ContaBancaria(titular, saldo)

# #Livro
# print("-"*20)
# print("Cadastro de Livro")
# titulo = input("Título: ")
# autor = input("Autor: ")
# ano_publicacao = int(input("Ano de publicação: "))

# livro = Livro(titulo, autor, ano_publicacao)

# #Curso
# print("-"*20)
# print("Cadastro de Curso")
# nome = input("Nome do curso: ") 
# duracao = input("Duração do curso (meses): ")
# instrutor = input("Instrutor do curso: ")

# curso = Curso(nome, duracao, instrutor)


# '''--------------- Atividade 04 ---------------
# Criar uma classe chamada Livro com os seguintes atributos:
# 1. Titulo
# 2. Autor
# 3. Ano
# Adicionar um método que exiba informações formatadas'''

# Livro
# class Livro:
#     def __init__(self, titulo, autor, ano):
#         self.titulo = titulo
#         self.autor = autor
#         self.ano = ano    

#     def info_format(self):
#         print("-" * 20)
#         print(f"Título: {self.titulo}")
#         print(f"Autor: {self.autor}")
#         print(f"Ano de Publicação: {self.ano}")
#         print("-" * 20)


# print("-" * 20)
# print("\nCadastro de Livro\n")
# print("-" * 20)

# while True:
#     try:
#         quantidade = int(input("Digite quantos livros deseja cadastrar: "))
#         if quantidade <= 0:
#             print("Por favor, digite um número positivo.")
#             continue
#         break
#     except ValueError:
#         print("Entrada inválida! Digite um número inteiro.")

# ListaLivros = []

# for i in range(quantidade):
#     print(f"\nCadastro do Livro {i + 1}")
#     titulo = input("Título: ")
#     autor = input("Autor: ")
#     ano_publicacao = int(input("Ano de publicação: "))
    
#     livro = Livro(titulo, autor, ano_publicacao)
#     ListaLivros.append(livro)

# print("\n--- Livros Cadastrados ---")
# for livro in ListaLivros:
#     livro.info_format()
