
# agrupe-os em 'baixo' (<=
# 2000), 'médio' (2001 - 5000) e 'alto' (> 5000). Armazene os resultados em um dicionário e
# exiba-o.
salarios = [1200, 2500, 4000, 7500, 10000]

dicio = {"alto":[], "medio":[], "baixo":[]}
for salario in salarios:
    if 2000<salario<=5000:
        dicio["medio"].append(salario)
    elif 5000<salario:
        dicio["alto"].append(salario)
    else:
        dicio["baixo"].append(salario)
#separa
print(dicio)