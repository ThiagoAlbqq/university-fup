# Faça uma função que, dada uma string, diga se ela é um palíndromo ou não. Lembrando que um palíndromo é uma palavra que tenha a propriedade de poder ser lida tanto da direita para a esquerda como da esquerda para a direita.
# Exemplos:
# ovo
# arara
# Socorram-me, subi no onibus em Marrocos.
# Anotaram a data da maratona

str1 = input()

def funcao(texto):
    texto = texto.replace(" ", "").replace("-", "").replace(",", "").replace(".", "").lower()

    for i in range(int(len(texto)/2)):
        if texto[i] != texto[len(texto) - 1 - i]:
            return False
        
    return True

print(funcao(str1))