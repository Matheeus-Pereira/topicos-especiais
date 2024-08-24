frase = "Python é incrível!"

def escreveVogal(texto):
    vogais = "aeiouAEIOUÉéíÍ"
    resultado = [] 

    # Percorre cada letra no texto
    for letra in texto:
        if letra in vogais:
            resultado.append(letra)
    
    # Conta o número de vogais
    contagem = len(resultado)
    
    # Exibe o resultado
    print("Vogais encontradas:", contagem, "\nElas são:", resultado)


escreveVogal(frase)
