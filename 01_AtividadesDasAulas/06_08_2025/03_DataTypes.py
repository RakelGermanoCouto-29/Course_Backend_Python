# --------------- ATIVIDADE 1 ---------------  

# Idade = 30

# Nome = "Maria"

# print(type(Idade))

# print(type(None))

# --------------- ATIVIDADE 2 ---------------  

# nome = input("Digite seu nome: ")
# print("Seu nome é: ", nome)

# idade = input("Digite sua idade: ")
# print("Sua idade é: ", idade)

# print("O tipo da sua variável é: ", type(idade))

# idadeFloat = float(idade)

# print("O tipo da sua variável float é: ", type(idadeFloat))

# --------------- ATIVIDADE 3 ---------------  
print("\n--------------- ATIVIDADE 3 ---------------\n")

nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
DataNascimento = (input("Digite sua Data de nascimento: "))
altura = float(input("Digite sua altura (Ex: 1.60): "))
sexo = input("Digite seu sexo (M/F): ")

print("Segue seus dados: \nNome:", nome,"\nIdade:", idade, "\nAltura:", altura, " m", "\nData de Nascimento:", DataNascimento)

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#---------------- ATIVIDADE 4 ---------------
#Média de notas
print("\n--------------- ATIVIDADE 4 ---------------\n")
N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))

media = (N1 + N2 + N3) / 3
#print("A média das notas é: ","{:.2f}".format(media))
print(f"A média das notas é: {media:.2f}")

# Verificando se o aluno foi aprovado ou reprovado
if media >= 7:
    print("Aluno aprovado!")
    aprovado = True
else:
    print("Aluno reprovado!")   
    aprovado = False

if sexo.upper() == "M":
    print("\nO estudante", nome, "tem", idade, "anos, sua altura é", altura, "e nasceu em", DataNascimento)
    print(nome, "foi", "aprovado" if aprovado else "reprovado", "com média", "{:.2f}".format(media))
elif sexo.upper() == "F":
    print("\nA estudante", nome, "tem", idade, "anos, sua altura é", altura, "e nasceu em", DataNascimento)
    print(nome, "foi", "aprovada" if media >= 7 else "reprovada", "com média", "{:.2f}".format(media))
else:
    print("Sexo inválido. Por favor, insira 'M' para masculino ou 'F' para feminino.")
