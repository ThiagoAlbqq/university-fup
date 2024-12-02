# 2. Crie uma função que permita fazer a conversão cambial de Dólares para Reais. Considere como taxa de câmbio US$ 1,0 = R$5,27.

def conversion(dol: float):
    return dol * 5.27

print(conversion(2))