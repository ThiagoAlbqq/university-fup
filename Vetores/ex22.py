# Exercício 22
# Preencha um vetor com os 100 primeiros naturais que não são múltiplos de 7 nem terminam em 7.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
contador = 1
while len(vetor) < 100:
    lastNum = contador % 10
    if not (contador % 7 == 0 or lastNum == 7):
        vetor.append(contador)
    contador += 1

print(vetor)
