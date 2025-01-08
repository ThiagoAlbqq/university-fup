# Faça uma função chamada de simplificada que receba como parâmetro o numerador e o denominador de uma fração. Esta função deve simplificar a fração recebida dividindo o numerador e denominador pelo maior fator possível. Por exemplo, a fração 36/60 simplificada para 3/5 dividindo o numerador e denominador por 12.

def simplificar(num, den):
    menor = num
    
    if den < menor:
        menor = den
    
    for i in range(menor, 1, -1):
        if num % i == 0:
            if den % i == 0:
                num = int(num / i)
                den = int(den / i)
                break
    return num, den
