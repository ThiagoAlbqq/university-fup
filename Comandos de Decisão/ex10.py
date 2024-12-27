# Ler um número inteiro entre 1 e 7
a = int(input("Digite um número entre 1 e 7: "))

# Verificar e imprimir o dia correspondente
if a == 1:
    print("Domingo")
elif a == 2:
    print("Segunda-feira")
elif a == 3:
    print("Terça-feira")
elif a == 4:
    print("Quarta-feira")
elif a == 5:
    print("Quinta-feira")
elif a == 6:
    print("Sexta-feira")
elif a == 7:
    print("Sábado")
else:
    print("Número inválido! Digite um número entre 1 e 7.")
