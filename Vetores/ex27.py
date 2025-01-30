# Exercício 27
# Crie uma função que recebe um vetor e remove os valores zero, compactando os elementos restantes.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = [1,2,3,0,0,1,0]

def funcao(vetor):
    while True:
        if vetor.count(0) > 0:
            vetor.remove(0)
        else:
            break
    return vetor

print(funcao(vetor))