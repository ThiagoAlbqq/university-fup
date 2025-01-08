# Escreva um programa que leia o nome e a idade de várias pessoas. Seu programa deve terminar quando uma idade negativa for digitada. Ao terminar, seu programa deve escrever o nome e a idade das pessoas mais jovens e mais velhas.

nMaior = ""
nMenor = ""
iMaior = 0
iMenor = 0
contador = 0

while True:
    nome = input()
    idade = int(input())
    if idade < 0:
        break
    
    if contador == 0:
        nMenor = nome
        nMaior = nome
        iMenor = idade
        iMaior = idade

    if iMenor > idade:
        iMenor = idade
        nMenor = nome
    if iMaior < idade:
        iMaior = idade
        nMaior = nome
    contador += 1

print(nMenor)
print(iMenor)
print(nMaior)
print(iMaior)