class Pessoa:
    def __init__(self, nome:str, altura:float, idade:int, etnia:str):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.etnia = etnia
    
    def falar(self):
        print(f"Olá, meu nome é {self.nome}.")
    def andar(self, distancia: float):
        print(f"Eu saí para caminhar. Voltarei quando completar {distancia} metros.")
    def cozinhar(self,receita:str):
        print(f"Estou cozinhando um(a) {receita}.")

#---------------------------------------------------------------------------------------

pessoa1 = Pessoa(nome= "Andressa de Vargas Fernandes", altura= 1.68, idade= 18, etnia="Branca")
pessoa1.falar()
pessoa1.cozinhar("Pizza de brócolis")
pessoa1.andar(1000)

class Principal:
    pessoa1 = Pessoa(nome= "Andressa", altura = 1.70, idade= 78, etnia="Calcasiano")
    pessoa1.falar()
    pessoa1.cozinhar("Feijão")
    pessoa1.andar(250)