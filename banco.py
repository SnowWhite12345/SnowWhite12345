class Banco:
    def __init__(self, numero:int, nome:str, saldo=0.0):
        self.__numero = numero
        self.__nome = nome
        self.__saldo = saldo

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self,numero):
        self.__numero = numero

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,saldo):
        self.__saldo = saldo

    def alterarNome(self):
        self.__nome = input("Digite o novo nome: ")

    def depositar(self):
        try:
            print(f"Valor de saldo: R$ {round(self.__saldo,2)}")
            self.saldo+=float(input("Digite o valor a ser depositado: "))
            print(f"Valor atual de saldo: R${round(self.__saldo,2)}")
        except ValueError:
            print("Valor de depósito inválido! Somente número (ex.: 3.99)")
            self.saldo+=float(input("Digite o valor a ser depositado: "))
            print(f"Valor atual de saldo: R${round(self.__saldo,2)}")
    
    def sacar(self):
        try:
            print(f"Valor de saldo: R$ {round(self.__saldo,2)}")
            self.saldo-=float(input("Digite o valor a ser sacado: "))
            print(f"Valor atual de saldo: R${round(self.__saldo,2)}")
        except ValueError:
            print("Valor de saque inválido! Somente número (ex.: 3.99)")
            self.saldo+=float(input("Digite o valor a ser sacado: "))
            print(f"Valor atual de saldo: R${round(self.__saldo,2)}")

#====================================================================================================================