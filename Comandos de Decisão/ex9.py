maior = -99999
meio = -99999
menor = 99999

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
