# 14. Faça uma função que receba um número inteiro positivo de três dígitos (de 100 a 999). 
# Retorne outro número formado pelos dígitos invertidos do número lido. 
# Exemplo: Entrada = 123, Saída = 321.

def invertAThree_placeNumber(number: int):
    hundreds = number // 100
    tens = number % 100 // 10
    units = number % 100 % 10
    newNumber = units * 100 + tens * 10 + hundreds
    return newNumber

print(invertAThree_placeNumber(123))
