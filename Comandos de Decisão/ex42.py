# Ler uma frase e contar quantos caracteres são brancos. Não use nenhuma funcionalidade do python que já faça isso.

contador = 0
str1 = input()

for i in range(len(str1)):
    if str1[i] == " ":
        contador += 1

print(contador)