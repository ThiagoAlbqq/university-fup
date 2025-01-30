A = int(input())
B = int(input())
C = int(input())

if A < B + C and B < A + C and C < A + B:
    if A == B == C:
        print("Triangulo equilatero")
    elif A == B or B == C or A == C:
        print("Triangulo isosceles")
    else:
        print("Triangulo escaleno")
else:
    print("Nao triangulo")
