# #---------------- ATIVIDADE 1 ---------------
# # Verifica se a pessoa é maior de idade ou não
# print("\n------------ Atividade 1 ------------\n")

# idade = int(input("Digite sua idade: "))

# if idade >= 18:
#     print("Você é maior de idade.")
# else:
#     print("Você é menor de idade.")

# #---------------- ATIVIDADE 2 ---------------
# # Verifica a nota do aluno e classifica o desempenho
# print("\n------------ Atividade 2 ------------\n")

# nota = float(input("Digite sua nota: "))

# if nota >= 9:
#     print("\nÓtimo")
# elif nota >= 7:
#     print("\nBom")
# elif nota >= 5: 
#     print("\nRegular")
# else:
#     print("\nRuim")

# #---------------- ATIVIDADE 3 ---------------
# # Verifica se a pessoa pode entrar em um evento com base na idade e ingresso
# # Acesso permitido para maiores de 18 anos com ingresso   

# print("\n------------ Atividade 3 ------------\n")

# idade = int(input("Digite sua idade: "))
# ingresso = input("Você possui ingresso? (s/n): ")

# if idade >= 18 and ingresso.lower() == 's':
#     print("Acesso permitido.")
# else:
#     print("Acesso negado.")

# if idade < 18:
#     print("Você é menor de idade, não pode entrar.")
# elif ingresso.lower() != 's':
#     print("Você não possui ingresso, não pode entrar.")
# elif idade < 18 and ingresso.lower() != 's':
#     print("Você é menor de idade e não possui ingresso, não pode entrar.")

# #---------------- ATIVIDADE 4 ---------------
# # Verifica a primeira letra do nome e se começa com 'A'
# # A primeira letra do nome é convertida para maiúscula

# print("\n------------ Atividade 4 ------------\n")

# nome = input("Digite seu nome: ")

# print("A primeira letra do seu nome é:", nome.upper()[0])

# if nome.upper().startswith('A'):
#     print("Seu nome começa com a letra A.")
# else:
#     print("Seu nome não começa com a letra A.")

# #---------------- ATIVIDADE 5 ---------------
# # Verifica se um número é par, ímpar, positivo ou negativo

# print("\n------------ Atividade 5 ------------\n")

# numero = int(input("Digite um número: "))
# if numero == 0:
#     print("O número digitado é zero.")
# else:
#     print ("O número digitado é: ", "par" if numero % 2 == 0 else "ímpar","\nO número digitado é: ", "positivo" if numero >=0 else "negativo")

# #---------------- ATIVIDADE 6 ---------------
# # Fórmula de baskara

# print("\n------------ Atividade 6 ------------\n")

# a = float(input("Digite o valor de a: "))
# b = float(input("Digite o valor de b: "))
# c = float(input("Digite o valor de c: "))

# delta = b**2 - 4*a*c

# if delta < 0:
#     print("A equação não possui raízes reais pois delta é menor que 0.")
#     print(f"\nDelta é: {delta:.2f}")
# elif delta == 0:
#     print("\nA equação possui uma raiz real pois delta é igual a 0.")
#     print(f"\nDelta é: {delta:.2f}")
#     raiz = (-b + delta**0.5) / (2 * a)
#     print(f"\nA raiz é: {raiz:.2f}")
# elif delta > 0:
#     print("\nA equação possui duas raízes reais pois delta é maior que 0.")
#     print(f"\nDelta é: {delta:.2f}")
#     raiz = (-b + delta**0.5) / (2 * a)
#     print(f"\nA raiz é: {raiz:.2f}")
    
#----------- Atividade 7 -----------
#Digite um numero para saber se ele é par, impar, positivo ou negativo. Digite 0 par aparar o código

print("Digite um número para saber se ele é par, impar, positivo ou negativo. Digite 0 par aparar o código.")

numero = int(input("Digite um número: "))

while numero != 0:
    print ("O número digitado é: ", "par" if numero % 2 == 0 else "ímpar","\nO número digitado é: ", "positivo" if numero >=0 else "negativo")
    numero = int(input("Digite um número: "))
    