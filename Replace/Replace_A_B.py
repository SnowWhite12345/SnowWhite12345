import tkinter as tk

def getReplace():
    str1 = "B"
    str2 = "#"

    cp1 = "Frase de entrada"
    cp2 = cp1.replace(str1, str2)
    return cp2

window = tk.Tk()
window.title("Swap")
window.geometry("300x300")

campo1 = tk.Entry(window)
campo1.place(x=50, y=30)
campo2 = tk.Entry(window)
campo2.place(x = 50, y=90)

lbl1 = tk.Label(window, text="Informe o alvo.")
lbl1.place(x=30, y=30)

lbl2 = tk.Label(window, text="Informe o substituto.")
lbl2.place(x=30, y=90)

window.mainloop()