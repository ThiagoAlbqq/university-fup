# 6. Elabore uma função para calcular o volume (V) de uma esfera e a área (A) de sua superfície, dado o valor de seu raio (R). 
# A fórmula do volume da esfera é V = 4/3 πRR3 e A = 4πRR2 .

import math

def calculateTheVolumeAndAreaOfBallWithTheRay(ray: float):
    volume = 4/3 * math.pi * ray ** 3
    area = 4 * math.pi * ray ** 2
    return volume, area

print(calculateTheVolumeAndAreaOfBallWithTheRay(2))