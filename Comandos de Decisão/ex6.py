# Faça um programa que leia 3 notas, verifique se as notas são válidas e exiba na tela a média destas notas com duas casas decimais. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.00 e 10.00, onde caso a nota não possua valor válido, este fato deve ser informado ao usuário e o programa termina.

cont = 3
soma = 0

while cont > 0:
    a = float(input("Digite um número entre 0 e 10: "))
    if 0 <= a <= 10:
        soma += a
        cont -= 1
    else:
        break

if cont == 0:
    media = soma / 3
    print(f"A média é: {media:.2f}")
else:
    print("A média não pôde ser calculada devido a entradas inválidas.")

