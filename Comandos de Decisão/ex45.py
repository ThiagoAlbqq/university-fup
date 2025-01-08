# O código de César é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, ‘A’ seria substituı́do por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente uma função que faça uso desse Código de César, entre com uma string e a quantidade de posições e retorne a string codificada. Exemplo:
# String: A LIGEIRA RAPOSA MARROM SALTOU SOBRE O CACHORRO CANSADO
# Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
# Observação: caso a letra codificada passe da letra Z, ela deve voltar para o início do alfabeto.

def funcao(texto, passos):
    resultado = list(texto)

    for char in range(len(resultado)):
        if 'A' <= resultado[char] <= 'Z':  # Se for uma letra maiúscula
            novo_char = chr((ord(resultado[char]) - ord('A') + passos) % 26 + ord('A'))
            resultado[char] = novo_char
        elif 'a' <= resultado[char] <= 'z':  # Se for uma letra minúscula
            novo_char = chr((ord(resultado[char]) - ord('a') + passos) % 26 + ord('a'))
            resultado[char] = novo_char
        else:
            # Deixe o caractere inalterado se não for uma letra
            resultado[char] = resultado[char]
    
    return "".join(resultado)

# Leitura do texto e número de passos
str1 = input("Digite o texto: ")
passos = int(input("Digite o número de passos: "))

# Codificação do texto
str1_codificada = funcao(str1, passos)

# Exibição do resultado
print(str1_codificada)
