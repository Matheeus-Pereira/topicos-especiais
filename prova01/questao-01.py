import tkinter as tk
from tkinter import messagebox

def calcular_juros():
    try:
        valor_inicial = float(valorini.get())
        taxa_juros = float(jurosano.get()) / 100  # Converter a porcentagem para decimal
        anos = int(tempo.get())
        
        # Cálculo do valor final usando juros simples
        valor_final = valor_inicial * (1 + taxa_juros * anos)
        
        # Exibir o resultado na tela
        resultado.config(text=f"O valor total é: R$ {valor_final:.2f}")
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira valores numéricos válidos.")


def escrever(x:str):
 label = tk.Label(janela, text=x)
 label.pack(pady=(15,0))


janela = tk.Tk()
janela.title("Calculadora de Juros Simples")
janela.geometry("400x300")

# valor inicial
escrever("valor inicial")
valorini = tk.Entry(janela, width=30)
valorini.pack(pady=0)

#  juros anual
escrever("Taxa de juros anual (%):")
jurosano = tk.Entry(janela, width=30)
jurosano.pack(pady=0)

#  tempo em anos
escrever('Anos passados:')
tempo = tk.Entry(janela, width=30)
tempo.pack(pady=0)


botao = tk.Button(janela, text="Calcular", command=calcular_juros)
botao.pack(pady=20)


resultado = tk.Label(janela, text="")
resultado.pack(pady=20)

# Iniciar o loop da janela
janela.mainloop()
