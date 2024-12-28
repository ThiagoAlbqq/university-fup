maior = float("-inf")
meio = float("-inf")
menor = float("inf")

cont = 3

while cont > 0:
    a = int(input("Digite um número: "))
    
    if a > maior:
        meio = maior
        maior = a
    elif a < menor:
        meio = menor
        menor = a
    else:
        meio = a

    cont -= 1

print(menor, meio, maior)
