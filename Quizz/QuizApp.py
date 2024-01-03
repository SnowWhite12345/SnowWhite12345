from tkinter import *
from tkinter import messagebox as mb 
import json

janela = Tk()
janela.geometry("800x400")
janela.title("Senac Quizz")

class Qsm:
    def __init__(self) -> None:
        self.perguntaNum = 0
        self.visTitulo()
        self.visQuest()
        self.escolha = IntVar
        self.opcao = self.radio_buttons()
        self.mostrar_opcoes()
        self.buttons()
        self.tam_dados = len(pergunta)
        self.correto = 0

    def VisResult(self) -> bool:
        cont_error = self.tam_dados - self.correto
        correto = f"Acertos: {self.correto}"
        erros = f"Erros: {cont_error}"
        score = float(round(self.correto/self.tam_dados*100,2))
        placar = f"Placar: {score}%"
        mb.showinfo("Resultado: \n", f"\n{correto}\n{erros}\n{placar}")

    def visPergunta(self, perguntaNum):
        if self.escolha.get() == resposta[perguntaNum]:
            return True

    def btnProx(self):
        if self.visPergunta(self.perguntaNum):
            self.correto +=1
            self.perguntaNum+=1

        if self.perguntaNum == self.tam_dados:
            self.VisResult()
            janela.destroy()
        else:
            self.visQuest()
            self.mostrar_opcoes()

    def buttons(self):
        btnProximo = Button(janela, text = "Próxima", command=self.btnProx, width= 10, bg= "black", fg= "white", font = ("Arial", 16, "bold"))
        btnProximo.place(x = 350, y = 350)

        btnEsc = Button(janela, text= "Sair", command= janela.destroy, width= 10, bg= "black", fg= "white", font = ("Arial", 16, "bold"))
        btnEsc.place(x=700, y=50)

        pass
    
janela.mainloop()    
    
    