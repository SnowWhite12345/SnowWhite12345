import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
from tkinter import *

frame = tk.Tk()
frame.geometry("300x250")
frame.resizable(False,False)
frame.title("Example Radio Button")
#frame.tk.call("wm", "iconphoto", frame._w, tk.PhotoImage(file="Radio.png"))


def VisEscolha():
    showinfo(title= "Resultado", message = f"Você escolheu {tam_Sel.get()}")

lPergunta = ttk.Label(text="Escolha o tamanho:", font=("Arial", 9, "bold"))
lPergunta.pack(fill="x", padx=15, pady=5)

tam_Sel = tk.StringVar(frame, value= "M")
tamanhos = (("Pequeno", "P"), 
            ("Médio", "M"), 
            ("Grande", "G"), 
            ("Grande Grande", "GG"),
            ("Extra Grande", "XG"), 
            ("Extra Extra Grande", "XXG"))

for tamanho in tamanhos:
    rd = ttk.Radiobutton(frame, text= tamanho[0], value= tamanho[1], variable= tam_Sel)
    rd.pack(fill = "x", padx=5, pady= 5)#Padding

bEscolha = ttk.Button(frame, text= "Ver tamanho", command=VisEscolha)
bEscolha.pack(fill="x", padx=5, pady=5)


frame.mainloop()