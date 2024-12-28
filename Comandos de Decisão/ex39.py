# Escreva um programa que leia duas palavras e diga qual delas vem primeiro na ordem alfabética. Não use nenhuma funcionalidade do python que já faça isso. Dica: ‘a’ é menor do que ‘b’.

def funcao(str1, str2):
    for i in range(min(len(str1), len(str2))):
        if str1[i] < str2[i]:
            return str1
        elif str1[i] > str2[i]:
            return str2
    
    if len(str1) < len(str2):
        return str1
    elif len(str1) > len(str2):
        return str2
    else:
        return str1

str1 = input()
str2 = input()

print(funcao(str1, str2))
