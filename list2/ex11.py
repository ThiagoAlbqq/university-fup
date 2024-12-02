# 11. Crie uma função que, dados três valores, retorne a soma dos quadrados dos três valores e o quadrado da soma dos três valores.

def calculateSquareOfSumAndSumOfSquare(num1: float, num2: float, num3: float):
    return num1** 2 + num2 ** 2 + num3 ** 2, (num1 + num2 + num3) ** 2

print(calculateSquareOfSumAndSumOfSquare(1,2,3))