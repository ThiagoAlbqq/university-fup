numero = int(input())
valid = False

if (numero % 3 == 0):
    if not(numero % 5 == 0):
        valid = True
elif (numero % 5 == 0):
    valid = True

print(valid)