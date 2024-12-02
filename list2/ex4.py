# 4. Faça uma função que, dado um número inteiro e retorne o seu antecessor e o seu sucessor.

def calculatePredecessorAndSucessor(number: int):
    return number - 1, number + 1

print(calculatePredecessorAndSucessor(2))