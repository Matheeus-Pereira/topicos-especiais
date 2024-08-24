# Dado a lista de idades: [4, 13, 18, 65, 30, 8, 17, 74] . Classifique cada idade em
# 'criança', 'adolescente', 'adulto' ou 'idoso'. Armazene os resultados em um dicionário e
# exiba-o. Onde até 12 anos é criança, entre 13 e 17 adolescente, entre 18 e 64 adulto e
# acima de 64 idoso.

idades = [4, 13, 18, 65, 30, 8, 17, 74]
idades.sort()
def processar(idades):
    classificao = {
        "criança":[], "adolescente":[], "adulto":[], "idoso":[]
    }
    for pessoa in idades:
        if pessoa <= 12:
            classificao["criança"].append(pessoa)
        elif 13  <=pessoa<=17:
           classificao["adolescente"].append(pessoa)
        elif 17<pessoa<=64:
            classificao["adulto"].append(pessoa)
        else:
            classificao["idoso"].append(pessoa)

    return classificao
#separação
print("idades: ",idades,"\n seperação por faixa etária:", processar(idades))

