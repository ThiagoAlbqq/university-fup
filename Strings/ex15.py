# 15. Faça uma função que receba um número inteiro de 4 dígitos (de 1000 a 9999) e retorne os 4 dígitos separados, cada um em uma variável diferente.

def cutAFour_placesNumber(number: int):
    thousands = number // 1000
    hundreds = number % 1000 // 100
    tens = number % 1000 % 100 // 10
    units = number % 1000 % 100 % 10
    return thousands, hundreds, tens, units

print(cutAFour_placesNumber(1234))