import os

pasta = "Comandos de Repeticao"
os.makedirs(pasta, exist_ok=True) # Caso a pasta não exista.

exercicios = [
    "1: Faça um programa que escreva na tela de 1 até 100.",
    "2: Escreva um programa que imprima os números de 0 até 100000 (cem mil), de 1000 em 1000.",
    "3: Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.",
    "4: Faça um programa que leia 10 inteiros e imprima sua média.",
    "5: Faça um algoritmo que imprima todos os números inteiros de 1 a N (fornecido pelo usuário).",
    "6: Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.",
    "7: Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido.",
    "8: Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.",
    "9: Faça uma função que calcule e retorne a soma dos N primeiros números pares (considere o 0 como o primeiro número par).",
    "10: Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule xn e retorne o resultado.",
    "11: Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.",
    "12: Escreva uma função que receba n e k tais que k ≥ 0 e n ≥ k e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)",
    "13: O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:\n    ◦ F1 = 1\n    ◦ F2 = 1\n    ◦ Fn = Fn−1 + Fn−2 para n> 2\n    Faça uma função que receba um valor inteiro n e calcule Fn.",
    "14: Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1/1 + 1/2 + 1/3 ... 1/n. Faça uma função que, dado um valor n inteiro positivo, calcule o valor de H(n).",
    "15: Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! ... 1/n!.",
    "16: Faça um programa que calcule e escreva o valor de S = 1/1 + 3/2 + 5/3 + 7/4 + ... + 99/50.",
    "17: Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex: ========). O programa deve ler quantos sinais de iguais serão mostrados.",
    "18: Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.",
    "19: Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).",
    "20: Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura.",
    "21: Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1.",
    "22: Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triângulo de Floyd.",
    "23: Faça um programa para exibir a tabuada de 1 a 9.",
    "24: O Triângulo de Pascal é um triângulo numérico infinito formado por números binomiais Cn,k, onde n representa o número da linha (posição horizontal) e k representa o número da coluna (posição vertical), iniciando a contagem a partir do zero.",
    "25: Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + ... + (n2 + 1)/(n + 3)",
    "26: Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n. Calcule o valor do seno desse ângulo usando a respectiva série de Taylor.",
    "27: Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número.",
    "28: Faça um programa que escreva 10 vezes na tela a seguinte mensagem: “Meu Curso é Show”.",
    "29: Faça um programa que leia um inteiro n ≥ 0 . Escreva n vezes a seguinte mensagem: “Estou sabendo Programar haha”.",
    "30: Faça um programa que receba uma palavra e a imprima de trás-para-frente.",
    "31: Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N. Concatene N vezes a string str2 ao final da string str1.",
    "32: Faça um programa que leia uma palavra e some 1 no valor ASCII de cada caractere da palavra. Imprima a string resultante."
]

for i, exercicio in enumerate(exercicios, 1):
    nome_arquivo = f"{pasta}/ex{i}.py"
    with open(nome_arquivo, 'w') as file:
        file.write(f"# Exercício {exercicio}\n\n")
        file.write("# Implemente aqui a solução do exercício\n")
        file.write("\n")
    print(f"Arquivo {nome_arquivo} criado com sucesso!")
