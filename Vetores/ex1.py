# Exercício 1
# Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso.
#--------------------------------------------------

# Escreva a solução aqui:
messes = [
    "janeiro",
    "fevereiro",
    "marco",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"
]

def funcao(data):
    split = data.split("/")
    mes = messes[int(split[1]) - 1]

    return f"{int(split[0])} de {mes} de {split[2]}"

print(funcao("01/01/2000"))