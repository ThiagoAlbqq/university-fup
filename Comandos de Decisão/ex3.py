# Ler 4 números inteiros e calcular a soma dos que forem par.

cont = 4
soma = 0
while cont > 0:
    a = int(input())
    soma += a if (a%2) == 0 else 0
    cont -= 1

print(soma)