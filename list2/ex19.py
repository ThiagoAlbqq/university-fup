# 19. Escreva uma função que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

def calculateSake(sake: int):
    hundreds = sake // 100
    fifty = sake % 100 // 50
    twenty = sake % 100 % 50 // 20
    ten = sake % 100 % 50 % 20 // 10
    five = sake % 100 % 50 % 20 % 10 // 5
    two = sake % 100 % 50 % 20 % 10 % 5 // 2
    one = sake % 100 % 50 % 20 % 10 % 5 % 2
    return hundreds, fifty, twenty, ten, five, two, one

print(calculateSake(11236))