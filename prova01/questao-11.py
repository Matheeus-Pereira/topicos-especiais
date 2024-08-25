frase = "Ana gosta de estudar e aprender novas coisas"
frase=frase.split()
vogal="aeiouAEIOU"
resultado=[]
for letra in frase:
  for v in vogal:
   if letra.startswith(v)and len(letra)>1:
       resultado.append(letra)
#separa

print("palavras começadas com vogais::",resultado)