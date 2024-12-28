# Faça um programa que conte o número de 1’s que aparecem em uma string. Exemplo: 0011001 -> 3. Não use nenhuma funcionalidade do python que já faça isso.

contador = 0
str1 = input()

for i in range(len(str1)):
    if str1[i] == "1":
        contador += 1

print(contador)