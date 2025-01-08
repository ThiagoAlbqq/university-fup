# Faça um programa que receba dois números. Calcule e mostre:
# A soma dos números pares desse intervalo de números (intervalo incluindo os números dados);
# A multiplicação dos números ímpares desse intervalo (intervalo incluindo os números dados)

sNP = 0
mNI= 1

n = int(input())
m = int(input())

if n <= m:
    for i in range(n, m+1):
        if i % 2 == 0:
            sNP += i
        else:
            mNI *= i
else:
    for i in range(m, n+1):
        if i % 2 == 0:
            sNP += i
        else:
            mNI *= i

print(sNP)
print(mNI)