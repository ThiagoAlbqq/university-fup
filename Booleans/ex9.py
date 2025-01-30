def funcao(num1, num2):
    if num1 <= num2:
        maior = num2
        menor = num1
    else:
        maior = num1
        menor = num2

    while menor != 0:
        maior, menor = menor, maior % menor
    mdc = maior
    
    mmc = (num1 * num2) // mdc
    return mmc
