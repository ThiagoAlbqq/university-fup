exercicios = [
    "Faça uma função que receba a data atual (dia, mês e ano em inteiro) e exiba-a na tela no formato textual por extenso.",
    "Crie um vetor A com 6 números inteiros e realize operações como soma, modificação e exibição.",
    "Leia 6 valores inteiros e exiba-os na tela.",
    "Leia 10 valores inteiros e exiba-os na ordem inversa.",
    "Armazene 10 números reais em um vetor e crie outro vetor com seus quadrados.",
    "Leia um vetor de 8 posições e dois índices X e Y, exibindo a soma dos valores dessas posições.",
    "Leia um vetor com 15 posições e conte quantos valores são pares.",
    "Leia um vetor com 15 posições e some os valores ímpares.",
    "Leia um vetor com 10 inteiros e exiba o maior e o menor valor.",
    "Leia um vetor de 20 inteiros e substitua os valores negativos por 0.",
    "Leia as notas de 15 alunos, calcule e exiba a média geral.",
    "Crie uma função que recebe um vetor de notas e retorna a média geral e o desvio padrão populacional.",
    "Crie uma função que recebe um vetor de notas e retorna a média, o desvio padrão e a quantidade de notas menores que 7.0.",
    "Preencha um vetor com 12 números reais aleatórios no intervalo [-10, 10] e conte quantos são negativos e some os positivos.",
    "Leia um vetor de 10 posições e verifique se há valores repetidos, exibindo-os.",
    "Crie uma função que recebe um vetor e retorna um novo vetor sem elementos repetidos.",
    "Crie uma função que recebe um vetor e um número X e retorna os múltiplos de X no vetor.",
    "Crie uma função que recebe dois vetores A e B e retorna um vetor C com a diferença A - B.",
    "Crie uma função que recebe dois vetores e retorna um vetor intercalando os valores.",
    "Leia um vetor de 100 números reais e exiba-o conforme um código de entrada (0 para sair, 1 para ordem normal, 2 para inversa).",
    "Preencha um vetor de tamanho 70 usando a fórmula (i + 5*i) % (i + 1) e exiba-o.",
    "Preencha um vetor com os 100 primeiros naturais que não são múltiplos de 7 nem terminam em 7.",
    "Leia 10 inteiros e exiba apenas os números primos e suas posições no vetor.",
    "Crie uma função que recebe dois vetores e retorna um vetor com a interseção sem elementos repetidos.",
    "Crie uma função que recebe dois vetores e retorna um vetor com a união sem elementos repetidos.",
    "Crie uma função que recebe dois vetores e retorna um vetor com a diferença (elementos do primeiro que não estão no segundo).",
    "Crie uma função que recebe um vetor e remove os valores zero, compactando os elementos restantes.",
    "Leia 12 inteiros diferentes e armazene-os, garantindo que não haja repetição.",
    "Crie uma função que ordena um vetor do maior para o menor sem usar funções de ordenação do Python.",
    "Crie uma função que identifica segmentos iguais máximos em um vetor e retorna suas posições e tamanho.",
    "Leia um nome e exiba quantas letras diferentes ele contém.",
    "Gerencie uma lista de até 5 nomes de alunos, permitindo buscas parciais e exibindo os índices encontrados."
]

for i in range(1, 33):
    with open(f"ex{i}.py", "w") as arquivo:
        arquivo.write(f"# Exercício {i}\n")
        arquivo.write(f"# {exercicios[i-1]}\n")
        arquivo.write("#" + "-" * 50 + "\n\n")
        arquivo.write("# Escreva a solução aqui:\n\n")
