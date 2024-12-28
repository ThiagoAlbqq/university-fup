# Escreva um programa que substitui as ocorrências de um caractere 0 em uma string pelo caractere 1. Não use nenhuma funcionalidade do python que já faça isso.

str1 = input()

str1_lista = list(str1)

for i in range(len(str1_lista)):
    if str1_lista[i] == "0":
        str1_lista[i] = "1"

str1 = "".join(str1_lista)

print(str1)