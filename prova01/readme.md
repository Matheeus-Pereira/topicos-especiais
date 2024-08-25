
*questões da prova*


1. Cálculo de juros simples. Defina variáveis para o valor inicial, a taxa de juros anual (em
decimal) e o tempo (em anos). Calcule o valor final de um investimento usando a fórmula
de juros simples: Valor Final = Valor Inicial * (1 + Taxa * Tempo) . Certifique-se
de que os valores informados sejam positivos e que a taxa de juros seja decimal (float,
algo como 0.05 ao ano). Casos todos valores sejam válidos imprima o resultado do juros,
caso algum valor não atenda os requisitos informe o que está errado.
2. Receba uma string via input , remova espaços e converta para minúsculas. Verifique se
a string é um palíndromo (ou seja, se a palavra é a mesma quando lida de trás para
frente). Exiba uma mensagem indicando se é ou não.
3. Dada a frase A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha
a rã. Nem a rã arranha a aranha. , conte quantas vezes cada palavra aparece.
Armazene os resultados em um dicionário e exiba-o. Deve fazer um saneamento dos
dados, considerando apenas palavras/letras, também deve ser considerado maiúsculas e
minúsculas iguais.
4. Dado a lista de idades: [4, 13, 18, 65, 30, 8, 17, 74] . Classifique cada idade em
'criança', 'adolescente', 'adulto' ou 'idoso'. Armazene os resultados em um dicionário e
exiba-o. Onde até 12 anos é criança, entre 13 e 17 adolescente, entre 18 e 64 adulto e
acima de 64 idoso.
5. Receba uma temperatura em Celsius via input e converta para Fahrenheit usando a
fórmula F = C * 9/5 + 32 . Exiba o resultado.
6. Dada a string Python é incrível! , conte o número de vogais. Exiba o total.
7. Simule o lançamento de dois dados e exiba a soma dos valores obtidos e o número da
tentativa a cada iteração. Repita até que a soma dos dados seja igual a 7 ou 11. Mostre
quantas tentativas foram necessárias para chegar a 7 ou 11 ao final do processo. Para
gerar o número do dado a cada iteração utilize random.randint(1, 6) , irá gerar um
número aleatório entre 1 e 6, importe o seguinte pacote import random para utilizar a
classe random.
8. Dado o dicionário valores = {"a": 10, "b": 20, "c": 30} , some todos os valores e
exiba o total.
9. Dada a string Python é poderoso! , conte o número de consoantes presentes. Exiba o
total.
10. Dada a lista de salários [1200, 2500, 4000, 7500, 10000] , agrupe-os em 'baixo' (<=
2000), 'médio' (2001 - 5000) e 'alto' (> 5000). Armazene os resultados em um dicionário e
exiba-o.
11. Dada a frase frase = "Ana gosta de estudar e aprender novas coisas" , conte
quantas palavras começam com uma vogal. Exiba o total
12. Dado o dicionário de estudantes e suas notas, classifique cada estudante em uma das
categorias de A a F, conforme a tabela abaixo:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
E: 50-59
F: abaixo de 50
Deve ser impresso a lista das notas classificadas e qual usuário possui essa
classificação de nota.
estudantes = {
"Alice": 85,
"Bob": 92,
"Charlie": 78,
"Diana": 88,
"Edward": 67,
"Fiona": 74,
"George": 53,
"Hannah": 59,
"Irene": 48,
"Jack": 95,
"Kelly": 84,
"Leo": 72,
"Mia": 64,
"Noah": 58,
"Olivia": 45
}
notas = {
'A': [],
'B': [],
'C': [],
'D': [],
'E': [],
'F': []
}
# resultado esperado: {'A': ['Bob', 'Jack'], 'B': ['Alice', 'Diana', 'Kelly'],
'C': ['Charlie', 'Fiona', 'Leo'], 'D': ['Edward', 'Mia'], 'E': ['George','Hannah', 'Noah'], 'F':['Irene', 'Olivia']
}