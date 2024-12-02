# 10. Crie uma função que, dado um ângulo em graus, retorne-o convertido em radianos. A fórmula de conversão é: R = G * π/180 , sendo G o ângulo em graus e R em radianos.

import math

def calculateAngleToRadians(angle: float):
    return angle * math.pi/180

print(calculateAngleToRadians(20))