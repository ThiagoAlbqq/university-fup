# Exercício 9: Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).

# Implemente aqui a solução do exercício
n = int(input())
sum = 0
for i in range(-1, n+1):
    if i % 2 == 0:
        sum +=i
print(sum)
