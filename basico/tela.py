import tkinter as tk

janela  = tk.Tk()

janela.title("janela teste")

janela.geometry("400x300") #largura x altura
# texto na janela

label = tk.Label(janela,text='janela simples' )
label.pack(pady=20)

test = tk.Entry(janela, width=30)
test.pack(pady=20)

#botão pra fechar 
botao = tk.Button(janela, text='fechar', command=janela.quit)
botao.pack(pady=10)

#loop inicial

janela.mainloop()