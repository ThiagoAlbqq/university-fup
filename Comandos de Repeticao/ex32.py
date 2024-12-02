# Exercício 32: Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante.

# Implemente aqui a solução do exercício
def funcao(palavra):
    nova_palavra = ""
    for caractere in palavra:
        nova_palavra += chr(ord(caractere) + 1)
    return nova_palavra
palavra = input()
resultado = funcao(palavra)
print(resultado)
