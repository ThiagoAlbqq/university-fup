# Faça um função para verificar se um número é positivo ou negativo. Sendo que o valor de retorno será 1 se positivo, −1 se negativo e 0 se for igual a zero.

def sinal(a):
    if a == 0: return 0
    if a > 0: return 1
    if a < 0: return -1
    return 999
