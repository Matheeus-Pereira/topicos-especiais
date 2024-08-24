import tkinter as tk
from tkinter import messagebox

# Criando a janela principal
janela = tk.Tk()
janela.title("Convertendo para minúsculas")
janela.geometry("400x300")

# Função para exibir um rótulo de texto
def escrever(x: str):
    label = tk.Label(janela, text=x)
    label.pack(pady=(15, 0))

# Função para processar o texto
def processar():
    try:
        entrada = frase.get().lower()  # Obtém o texto da Entry em minúsculas
        resultado.config(text=f"O texto digitado em minúsculas é:\n{entrada}")

        # Remove espaços e verifica se é um palíndromo
        pali = entrada.replace(" ", "")
        if pali == pali[::-1]:
            resultado.config(text=resultado.cget("text") + "\nEsta frase é um palíndromo!")
        else:
            resultado.config(text=resultado.cget("text") + "\nEsta frase não é um palíndromo.")
    
    except ValueError:
        messagebox.showwarning("Entrada inválida", "Por favor, insira uma frase válida.")

# Adiciona o rótulo e a entrada de texto
escrever("Digite aqui:")
frase = tk.Entry(janela, width=30)
frase.pack(pady=0)

# Botão para processar
botao = tk.Button(janela, text="Processar", command=processar)
botao.pack(pady=0)

# Rótulo para exibir o resultado
resultado = tk.Label(janela, text="")
resultado.pack(pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()
