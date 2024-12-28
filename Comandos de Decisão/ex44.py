# Faça um programa que receba uma frase e imprima-a de maneira invertida, trocando as letras A (maiúsculas ou minúsculas) por *. Não use nenhuma funcionalidade do python que já faça isso.

str1 = input()
str1_lista = list(str1)

# se precisar inverter                                     str1_invertida = str1[::-1]

for i in range(len(str1_lista)):
    if str1_lista[i] == "A" or str1_lista[i] == "a":
        str1_lista[i] = "*"

str1 = "".join(str1_lista)

print(str1)