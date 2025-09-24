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


