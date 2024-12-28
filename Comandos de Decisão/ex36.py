# Faça uma função que retorne o maior fator primo de um número
# Essa aqui é complicada, mas vendo todo dia vc entende...

def funcao(n):
    maior_fator = 1
    while n % 2 == 0:
        maior_fator = 2
        n //= 2

    fator = 3
    while fator * fator <= n:
        while n % fator == 0:
            maior_fator = fator
            n //= fator
        fator += 2
    
    if n > 2:
        maior_fator = n
    
    return maior_fator
