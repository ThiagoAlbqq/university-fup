# Ler 4 números inteiros e calcular a soma dos que forem par.

cont = 4
soma = 0
while cont > 0:
    a = int(input())
    if (a % 2) == 0:
        soma += a
    cont -= 1

print(soma)