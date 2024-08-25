frase = "Ana gosta de estudar e aprender novas coisas"

vogal="aeiouAEIOU"
resultado=[]
for letra in frase:
 if letra in vogal:
  resultado.append(letra)
#separa

print("vogais: encontradas:",resultado, "\ntotal de de vogais:" ,len(resultado))