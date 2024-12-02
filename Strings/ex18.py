# 18. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido proporcionalmente ao valor que cada deu para a realização da aposta. 
# Faça uma função que receba quanto cada apostador investiu e o valor do prêmio, e retorne quanto cada um ganharia do prêmio com base no valor investido.

def calculateDivisionOfAward(winner1: float, winner2: float, winner3: float, award: float):
    contributed = winner1 + winner2 + winner3
    award1 = winner1/contributed * award
    award2 = winner2/contributed * award
    award3 = winner3/contributed * award
    return award1, award2, award3

print(calculateDivisionOfAward(25,25,50,1000))