frase = "Python é incrível!"

def achaConsoantes(x:str):

 consoantes ="bcdfghjklmnpqrstwxyzBCDFGHJKLMNPQRSTVWXYZ"
 result = []
 for letra in x:
    if letra in consoantes:
     result.append(letra)
   
 conta = len(result)
 print("consoantes encontradas:",result,"\nquantidade de consoantes encontradas:", conta)

achaConsoantes(frase)