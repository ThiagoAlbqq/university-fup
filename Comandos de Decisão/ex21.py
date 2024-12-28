# Faça uma função que receba dois números e retorne qual deles é o maior.

a = input()
b = input()

def funcao(a,b):
    if a == b:
        print("Números iguais")
    else:
        if a > b:
            return a
        else: 
            return b
        
funcao(a,b)
