import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()
janela.title("Convertendo Celsius para fahrenheit")

janela.geometry("400x300")

def escrever(x: str):
    label = tk.Label(janela, text=x)
    label.pack(pady=(15, 0))
#separação

def processar():
    try:
        entrada = float(temperatura.get())
        faren = (entrada*9/5)+32
        resultado.config(text=f"O valor dessa temperatura em fahrenheit é de:{faren:.2f}º")
    except ValueError:
        messagebox.showwarning("entrada inválida!!")
#separação
escrever("digite a temperatura em calsius (º)")
temperatura = tk.Entry(janela, width=30)
temperatura.pack(pady=0)

botao = tk.Button(janela, text="converter",command=processar)
botao.pack(pady=20)

resultado = tk.Label(janela, text="")
resultado.pack(pady=20)

janela.mainloop()