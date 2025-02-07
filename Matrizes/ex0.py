exercicios = [
    "Leia uma matriz 4 × 4 de inteiros, conte e escreva quantos valores maiores que 10 ela possui.",
    "Leia um número n e crie uma matriz n×n. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida, em forma de tabela. Use comandos de repetição.",
    "Faça um programa que preenche uma matriz de tamanho nxn com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz, em forma de tabela.",
    "Leia uma matriz 4 × 4, imprima a matriz, imprima a localização (linha e coluna) do maior valor e imprima o maior valor.",
    "Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de 'Não encontrado'.",
    "Leia duas matrizes 4 × 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas.",
    "Gerar e imprimir uma matriz A de tamanho 10 × 10, onde seus elementos são da forma: A[i][j] = 2 * i + 7 * j - 2, se i < j; A[i][j] = 3 * i ** 2 - 1, se i = j; A[i][j] = 4 * i ** 3 - 5 * j ** 2 + 1, se i > j.",
    "Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão acima da diagonal principal. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão abaixo da diagonal principal. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão na diagonal principal. Use apenas um comando de repetição. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão na diagonal secundária. Use apenas um comando de repetição. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Leia uma matriz 4 × 4. Calcule e imprima sua transposta. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Faça um programa que permita ao usuário entrar com uma matriz de 5 × 5 números reais. Em seguida, gere um vetor unidimensional contendo a soma dos números de cada coluna da matriz e mostre na tela esse vetor.",
    "Faça um programa que leia duas matrizes A e B de tamanho 4 × 5 cada uma. Calcule a matriz C = A + B. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Faça um programa que leia duas matrizes A e B de tamanho 5 × 5 cada uma. Calcule a matriz C = A * B. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.",
    "Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada linha pelo maior elemento em módulo daquela linha. Escreva a matriz original e a modificada.",
    "Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada coluna pelo maior elemento daquela coluna que seja primo. Caso a coluna não possua um número primo, divida a coluna pelo menor número da coluna. Escreva a matriz original e a modificada. Obs.: Números negativos também podem ser primos.",
    "Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de uma semente dada como entrada. Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada. Não use nenhum comando de decisão (se/então/senão).",
    "Faça um programa que gere uma matriz m × n de inteiros aleatórios. Mostre a matriz e calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como entrada para o programa.",
    "Na matriz de 20 × 20 abaixo, quatro números ao longo de uma diagonal foram marcados em negrito. O produto desses números é 26 × 63 × 78 × 14 = 1788696. Qual é o maior produto de quatro números adjacentes em qualquer direção (vertical, horizontal ou diagonal) na matriz de 20 × 20? A matriz 20 × 20 será dada como entrada, e o programa deve exibir o valor da multiplicação, a posição (linha e coluna) de onde começam os números, e a direção (cima, baixo, esquerda, direita, direita cima, esquerda cima, direita baixo, esquerda baixo)."
]

for i in range(1, len(exercicios)):
    with open(f"ex{i}.py", "w") as arquivo:
        arquivo.write(f"# Exercício {i}\n")
        arquivo.write(f"# {exercicios[i-1]}\n")
        arquivo.write("#" + "-" * 50 + "\n\n")
        arquivo.write("# Escreva a solução aqui:\n\n")
