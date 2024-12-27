#  Faça uma função para verificar se um número é um quadrado perfeito. Ex: 1, 4, 9...
import math

a = float(input())

def quadradoPerfeito(a):
    if int(math.sqrt(a)) * int(math.sqrt(a)) == a:
        return True
    return False

print(quadradoPerfeito(a))