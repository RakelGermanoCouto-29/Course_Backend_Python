#Dicionários

# Aluno = {
#     "nome" : "Carlos",
#     "idade" : 18,
#     "nota" : 6.5
#     #"Chave" : valor,
# }
# print(Aluno)
# print(Aluno["nome"])

# Aluno["idade"] = 21
# Aluno["curso"] = "python"

# print(Aluno)

# print("-"*50)

# for chave in Aluno:
#     print(f"{chave} : {Aluno[chave]}")

# print(Aluno.keys())
# print(Aluno.values())
# print(Aluno.items()) #Lista de tuplas
# print(len(Aluno))

# print("Sim" if "nome" in Aluno else "não")
# print("Sim" if "telefone" in Aluno else "não")

# del Aluno["curso"]

# print(Aluno)

# print(Aluno.get("email","n/a"))

# Aluno.update({"email":"email.gmail.com"})

# print(Aluno.get("email","n/a"))

# Idade = Aluno.pop("idade")

# print(Idade, Aluno)

#Atividade teste

# elemento = {
#     "Z" : 5,
#     "nome" : "cesio",
#     "grupo" : "metais",
#     "desidade" : 8.76
# }

# print("Elemento: ",elemento["grupo"])

# print(len(elemento))

# elemento["massa"] = 2

# print(elemento, len(elemento))


# for chave, i in elemento.items():
#     print(chave,":",i)

# for i in elemento.keys():
#     print(i)

# for i in elemento.values():
#     print(i)

#Conjuntos

# numeros = {1, 2, 3, 4}
# print(numeros)

# A = {1, 2, 3}
# B = {3, 4, 5}

# print(A|B)#União
# print(A&B)#Interseção
# print(A-B)#Diferença
# print(B-A)
# print(A^B)#Estão em A ou B mas não em ambos
# print(A<=B)#Se todos os elementos de A estão em B

# A = {3, 4}
# print(A<=B)

#bairros = {"guanabara", "oeste", "itatiaia", "bueno"}

# for bairro in bairros:
#     print(bairro.upper())
#     print(bairro.lower())

#Transformando listas em conjuntos

# numeros = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
# print(numeros)

# numerosConjunto = set(numeros)

# print(numerosConjunto  )

#------------- Atividade 1 -----------

# Livro = {
#     "Titulo" : "Python para iniciantes",
#     "Autor" : "Ana Silva",
#     "Ano" : "2023"
# }

# for chave, i in Livro.items():
#     print(f"{chave} : {i}")

#------------- Atividade 2 -----------

# Agenda = {
#     "Rakel" : "(62) 9 9999-1111",
#     "Guilherme" : "(62) 9 9999-2222",
#     "João" : "(62) 9 9999-3333"
# }

# for chave, i in Agenda.items():
#     print(f"Nome: {chave} Contato: {i}\n{"-"*20}")

#------------- Atividade 3 -----------

Cadastro1 = {
    "Nome" : "Rakel",
    "Idade" : 23,
    "Curso" : "Engenharia"
}

Cadastro2 = {
    "Nome" : "João",
    "Idade" : 18,
    "Curso" : "História"
}

Cadastro3 = {
    "Nome" : "Victor",
    "Idade" : 15,
    "Curso" : "Matemática"
}

CadastroGeral = [Cadastro1, Cadastro2, Cadastro3]

ordenado = sorted(CadastroGeral, key=lambda a:a["Idade"])

for Cadastro in ordenado:
    #print(f"Filme: {filme["Titulo"]}")
    for chave, value in Cadastro.items():
        print(f"{chave} : {value}")
        
    print("-"*20)

#------------- Atividade 4 -----------

# lista = ["rakel", "carlos", "joão", "felipe", "carlos", "junior", "rakel"]

# conjunto = set(lista)

# print(conjunto)
# print(sorted(conjunto))

#------------- Atividade 5 -----------

# filmes = [{"Titulo" : "Matrix","ano" : 1999},{"Titulo" : "Senhor do anéis","ano":2001}, 
#           {"Titulo" : "Cars","ano":2005}]
        


# for filme in filmes:
#     #print(f"Filme: {filme["Titulo"]}")
#     for chave, value in filme.items():
#         print(f"{chave} : {value}")
        
#     print("-"*20)
