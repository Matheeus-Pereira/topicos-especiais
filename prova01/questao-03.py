# Dada a frase A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha
# a rã. Nem a rã arranha a aranha. , conte quantas vezes cada palavra aparece.
# Armazene os resultados em um dicionário e exiba-o. Deve fazer um saneamento dos
# dados, considerando apenas palavras/letras, também deve ser considerado maiúsculas e
# minúsculas iguais.

frase="A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha"
print(frase)

print(len(frase))

palavras = frase.split()
dicionario ={}
for letra in palavras:
    letra = letra.lower()
    if letra in dicionario:
        dicionario[letra]+=1
    else:
        dicionario[letra] = 1
#separa
repete = {letra:dicionario[letra] for letra in dicionario if dicionario[letra]>1}

print(repete)