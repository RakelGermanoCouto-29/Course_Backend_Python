# #---------------- ATIVIDADE 1 ---------------

# for i in range(1, 5):
#     print(f"\n------------ Atividade {i} ------------\n")


# for i in "Rakel":
#     print(i)
#     if i == "k":
#         break

# for i in range(5, 10):
#     print(i)

# print(50*'-')

# print("A"," rakel"," fala"," de"," mais", sep = "-")

# nomes = ["Rakel", "João", "Maria", "Pedro"]

# for i in nomes:
#     print(i, end="; \n")

# for i, nome in enumerate(nomes, start=1):
#     print(f"{i} - {nome}", end = "; \n")

# #desafio: a pesso adigita um numero e tem 5 changes 
# # para o outro usuário acertar o numero. O numero é de 1 a 100

# print("Faça sua aposta!!")
# numero = 0


# while numero < 1 or numero > 100:
#     numero = int(input("Digite um número de 1 a 100:"))

# tentativas = 0



# print("\n ** SORTE **"*10)

# while tentativas < 5:
#     teste = int(input("Digite seu número da sorte da 1 a 100: "))
    
#     if 1 <= teste <= 100:
#         tentativas += 1
#         if teste == numero:
#             print("Parabéns! Você acaba de ganhar nota 100 na atividade do curso!")
#             break
#         elif teste != numero and tentativas < 5:
#             print(50*"\n")
#             print("Errou, tente novamente.")
#         elif teste != numero and tentativas >= 5:
#             print("Não foi dessa vez! Aposte novamente e tenha mais chances de ganhar!")
#     else:
#         print("O número deve ser de 1 até 100.")

#desafio: a pesso adigita um numero e tem 5 changes 
# para o outro usuário acertar o numero. O numero é de 1 a 100

# import random

# print("Faça sua aposta!!")
# numero = random.randint(1, 101)

# print(numero)

# while True:
#     for i in range(1, 6):
#         teste = int(input(f"Tentativa {i}, digite o numero:"))
#         if teste == numero:
#             print("Parabéns, você acertou!!")
#             break
#         elif teste < 1 or teste > 100:
#             print("O seu numero está fora do range de 1 até 100.")
#         elif teste != numero:
#             if teste < numero:
#                 print("O número correto é maior!!")
#             elif teste > numero:
#                 print('O número correto é menor!!')
#     if teste != numero:
#         print("Infelizmente você usou todas as suas tentativas.")
#     break

lista = ["Rakel", "João", "Victor"]

for i, nomes in enumerate(lista, start=1):
    print(i, nomes, sep = " - ", end = "; ")
print("\n")
for i, nomes in enumerate(lista, start=1):
    print(i, nomes, sep = " - ", end = "\n")

# import random

# while True:
    
#     print("Faça sua aposta!!")
#     numero = random.randint(1, 101)

#     print(numero)
#     for i in range(1, 6):
#         teste = int(input(f"Tentativa {i}, digite o numero:"))
#         if teste == numero:
#             print("Parabéns, você acertou!!")
#             break
#         elif teste < 1 or teste > 100:
#             print("O seu numero está fora do range de 1 até 100.")
#         elif teste != numero:
#             if teste < numero:
#                 print("O número correto é maior!!")
#             elif teste > numero:
#                 print('O número correto é menor!!')
#     if teste != numero:
#         print("Infelizmente você usou todas as suas tentativas.")
#         continuar = input("Quer continuar jogando: (Sim or Nao)")
#         if continuar.upper() == "NAO":
#             break
#     else:
#         continuar = input("Quer continuar jogando: (Sim or Nao)")
#         if continuar.upper() == "NAO":
#             break