# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

num = int(input())
den = int(input())

menor = num

if den < menor:
    menor = den

for i in range(menor, 1, -1):
    if num % i == 0 and den % i == 0:
        num = int(num / i)
        den = int(den / i)
        break

print(num, den)
