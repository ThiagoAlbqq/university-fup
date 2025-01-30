# Exercício 28
# Leia 12 inteiros diferentes e armazene-os, garantindo que não haja repetição.
#--------------------------------------------------

# Escreva a solução aqui:


vetor = []
while len(vetor) < 12:
    num = int(input())

    if num not in vetor:
        vetor.append(num)
    else:
        print(f"Numero {num} ja existe, escreva outro")

print(vetor)