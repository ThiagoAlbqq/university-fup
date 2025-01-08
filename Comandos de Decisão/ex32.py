# Faça um algoritmo que, dados dois números inteiros, seja capaz de obter o quociente inteiro da divisão entre o maior e o menor deles. Não use a operação de divisão (/), nem a operação de divisão inteira (//) e nem a operação de resto da divisão inteira (%).

cont = 0

n1 = int(input())
n2 = int(input())

if n1 >= n2:
    while True:
        if n2 * cont > n1:
            cont -= 1
            break
        else:
            cont += 1
else:
    while True:
        if n1 * cont > n2:
            cont -= 1
            break
        else:
            cont += 1 
    
print(cont)