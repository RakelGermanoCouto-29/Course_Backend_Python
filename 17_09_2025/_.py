# # Classe base
# class Jogador:
#     def __init__(self, altura, velocidade, passe, drible, precisao):
#         self.altura = altura
#         self.velocidade = velocidade
#         self.passe = passe
#         self.drible = drible
#         self.precisao = precisao

#     def passar(self):  
#         print("Mirar")
#         print("Encostar na bola com a força de passe do jogador")

#     def chutar(self):
#         print("Mirar")
#         print("Encostar na bola com 2x a força de passe do jogador")

#     def defender(self):
#         print("Defender de forma genérica")

# # Subclasse: Goleiro
# class Jogador_Goleiro(Jogador):
#     def agarrar(self):
#         print("Pular")
#         print("Se esticar para pegar a bola")

#     def defender(self):
#         esta_fora_area = False
#         if esta_fora_area:
#             print("Usar apenas os pés, cabeça, ombro")
#         else:
#             print("Usar qualquer parte do corpo")
#         print("Tentar tirar a bola do adversário")

# # Subclasse: Jogador de Linha
# class Jogador_Linha(Jogador):
#     def correr(self):
#         print("Consegue mudar de direção rapidamente")
#         print("Altera velocidade entre rápido e lento, dependendo da jogada")

#     def defender(self):
#         print("Usar apenas os pés, cabeça, ombro")
#         print("Tentar tirar a bola do adversário")

# # Criando objetos
# jogador1 = Jogador_Goleiro(180, 60, 80, 20, 60)
# jogador2 = Jogador_Linha(174, 90, 80, 85, 80)

# # === HERANÇA ===
# print('=== HERANÇA ===\n')
# print('Goleiro' + '\n' + '-' * 50)

# # passar() é herdado da classe Jogador — aqui mostramos a herança em ação
# jogador1.passar()
# print('\n' + 'Jogador de linha' + '\n' + '-' * 50)

# # passar() também é herdado pelo jogador de linha
# jogador2.passar()

# # === MÉTODOS ESPECÍFICOS DAS SUBCLASSES ===
# print('\n=== MÉTODOS ESPECÍFICOS DAS SUBCLASSES ===\n')
# print('Goleiro' + '\n' + '-' * 50)
# jogador1.agarrar()
# print('\n' + 'Jogador de linha' + '\n' + '-' * 50)
# jogador2.correr()
# # === POLIMORFISMO ===
# print('\n=== POLIMORFISMO ===\n')
# # Chamamos o mesmo método defender() em objetos de classes diferentes
# # e cada um executa sua versão (comportamento diferente).
# for p in (jogador1, jogador2):
#     print(p.__class__.__name__ + '\n' + '-' * 50)
#     p.defender()



# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
#     def falar(self):
#         print("Som genérico")
# class Cachorro(Animal):
#     def falar(self):
#         print("Au au!")
# # Criando instâncias
# animal = Animal("Animal genérico")
# cachorro = Cachorro("Rex")
# # Chamando métodos
# animal.falar()
# print("-")
# cachorro.falar()
# print("-")
# print(cachorro.nome) # Atributo herdado
# print("-")
# print(animal.nome) # Atributo herdado



#ATIVIDADE 1

# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario
    
#     def exibir_info(self):
#         return f"{self.nome} recebe {self.salario} reais."

# class Gerente(Funcionario):
#     def __init__(self, nome, salario, Nome_Departamento):
#         super().__init__(nome, salario)
#         self.Nome_Departamento = Nome_Departamento
        
#     def exibir_info(self):
#         return f"{self.nome} é gerente, recebe {self.salario} e é do departamento {self.Nome_Departamento}"

# class Desenvolvedor(Funcionario):
#     def __init__(self, nome, salario, lingua_falada):
#         super().__init__(nome, salario)
#         self.lingua_falada = lingua_falada
        
#     def exibir_info(self):
#         return f"{self.nome} é desenvolvedor, recebe {self.salario} e programa em {self.lingua_falada}"


# func = Funcionario("Ana", 3000)
# ger = Gerente("Carlos", 8000, "TI")
# dev = Desenvolvedor("Maria", 5000, "Python")

# print("-"*50)
# print(func.exibir_info())
# print("-"*50)
# print(ger.exibir_info())
# print("-"*50)
# print(dev.exibir_info())
# print("-"*50)


#Atividade 2
# class Veiculo:
#     def __init__(self, marca, velocidade):
#         self.marca = marca
#         self.velocidade = velocidade
    
#     def mover(self):
#         return f"Veícilo da marca {self.marca} se movendo."

# class Carro(Veiculo):      
#     def LigarMotor(self):
#         return f"O veículo é um carro da marca {self.marca}, velocidade {self.velocidade} km por h e você deve ligar o motor. "

# class Bicicleta(Veiculo):
#     def Pedalar(self):
#         return f"O veículo é uma bicicleta da marca {self.marca}, velocidade {self.velocidade} km por h e você deve pedalar. "

# veiculo = Veiculo("veículo", 0)
# carro = Carro("Fiesta", 250)
# bicicleta = Bicicleta("Caloi", 20)

# print("-"*50)
# print(veiculo.mover())

# print("-"*50)
# print(carro.LigarMotor())

# print("-"*50)
# print(bicicleta.Pedalar())

# print("-"*50)
# print("-"*50)


# # Teste das classes
# carros = [
#     Carro("Toyota", 120),
#     Carro( "Ford", 150)
# ]

# # Teste das classes
# bicicletas = [
#     Bicicleta("Caloi", 20),
#     Bicicleta( "bike", 15)
# ]
# for v in carros:
#     print(v.LigarMotor())
#     print("-"*50)

# for v in bicicletas:
#     print(v.Pedalar())
#     print("-"*50)

#Atividade 3

# class Politico:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
    

# class Vereador(Politico):
#     def __init__(self, nome, idade, municipio):
#         super().__init__(nome, idade)
#         self.municipio = municipio
    
#     def local(self):
#         return f"O vereador {self.nome}, {self.idade} anos, atua em {self.municipio}"
    

# class Presidente(Politico):
#     def __init__(self, nome, idade, pais):
#         super().__init__(nome, idade)
#         self.pais = pais
    
#     def local(self):
#         return f"O Presidente {self.nome}, {self.idade} anos, atua em {self.pais}"


# vereadores = [
#     Vereador("Major Vitor Hugo", 48, "Goiânia"),
#     Vereador("Rose Cruvinel", 76, "Goiânia"),
#     Vereador("Tião Peixoto", 79, "Goiânia")
# ]

# presidentes = [
#     Presidente("Luiz Inácio Lula da Silva", 79, "Brasil"),
#     Presidente("Joe Biden", 82, "Estados Unidos"),
#     Presidente("Emmanuel Macron", 47, "França")
# ]

# for v in vereadores:
#     print(v.local())
#     print("-"*50)

# for v in presidentes:
#     print(v.local())
#     print("-"*50)

#Atividade 4


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina, salario):
        super().__init__(nome, idade)
        self.disciplina = disciplina
        self.salario = salario
    
    def Apresentar(self):
        return f"O Professor {self.nome}, {self.idade} anos, ministra a disciplina {self.disciplina} e recebe {self.salario} reais."
    

class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula, curso):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.curso = curso

    def Apresentar(self):
        return f"O Aluno {self.nome}, {self.idade} anos, matriculado no número {self.matricula} é do curso {self.curso}."


professores = [
    Professor("Ronaldo", 48, "Python", 4000),
    Professor("Rafael", 43, "Matemática", 3000),
    Professor("Thiago", 39, "Geografia", 2500)
]

alunos = [
    Aluno("Rakel", 23, "20201010", "Python"),
    Aluno("Guilherme", 24, "20191010", "Mecânica"),
]

print("------ PROFESSORES ------")
for v in professores:
    print(v.Apresentar())
    print("-"*50)

print("------ ALUNOS ------")

for v in alunos:
    print(v.Apresentar())
    print("-"*50)


