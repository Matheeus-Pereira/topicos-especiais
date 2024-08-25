# Simule o lançamento de dois dados e exiba a soma dos valores obtidos e o número da
# tentativa a cada iteração. Repita até que a soma dos dados seja igual a 7 ou 11. Mostre
# quantas tentativas foram necessárias para chegar a 7 ou 11 ao final do processo. Para
# gerar o número do dado a cada iteração utilize random.randint(1, 6) , irá gerar um
# número aleatório entre 1 e 6, importe o seguinte pacote import random para utilizar a
# classe random.

import random

interacao = 0

while True:
    interacao += 1
    dado01 = random.randint(1, 6)
    dado02 = random.randint(1, 6)
    soma = dado01 + dado02

    print(f"Tentativa {interacao}: dado01 = {dado01}, dado02 = {dado02}, soma = {soma}")

    # Verifica se a soma é igual a 7 ou 11
    if soma == 7 or soma == 11:
        break

print(f"Soma igual a {soma} obtida após {interacao} tentativas.")
