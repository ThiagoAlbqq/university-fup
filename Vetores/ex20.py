# Exercício 20
# Leia um vetor de 100 números reais e exiba-o conforme um código de entrada (0 para sair, 1 para ordem normal, 2 para inversa).
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
for i in range(100):
    vetor.append(float(input()))
    
while True:
    
    code = int(input())
    if code == 0:
        break

    if code == 1:
        for i in range(len(vetor)):
            print(vetor[i])
    elif code == 2:
        for i in range(len(vetor)-1, -1, -1):
            print(vetor[i])
    else:
        print("Codigo invalido")