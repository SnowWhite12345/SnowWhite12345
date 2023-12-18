class Aluno:
    def __init__(self, nome:str, matrícula:int, notas: list):
        self.nome = nome
        self.matrícula = matrícula
        self.notas = notas

    def nomealuno(self):
        print(f"Nome: {self.nome}")
    def matricula(self):
        print(f"Matrícula: {self.matrícula}")
    def nota(self):
        print(f"Notas: {self.notas}")
        print(f"Média final: {round(sum(self.notas)/len(self.notas),1)}")
   
aluno1 = Aluno(nome="Andressa de Vargas Fernandes", matrícula=938542, notas= [9.2, 8.3, 3.4, 5.5, 6.3])
aluno1.nomealuno()
aluno1.matricula()