# Crie uma função que diga se duas strings são iguais ou não, analisando caractere a caractere.

str1 = input()
str2 = input()

def funcao(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
        
    return True

print(funcao(str1, str2))