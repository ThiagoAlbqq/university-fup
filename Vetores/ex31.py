# Exercício 31
# Leia um nome e exiba quantas letras diferentes ele contém.
#--------------------------------------------------

# Escreva a solução aqui:

nome = input()
diferentes = []
for char in nome:
    if char.isalpha() and char not in diferentes:
        diferentes.append(char)
print(len(diferentes))
