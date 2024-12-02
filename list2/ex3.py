# 3. Faça uma função que, a partir das medidas dos lados de um retângulo, calcule a área e o perímetro deste retângulo.

def calculateAreaAndPerimeter(side1: float, side2: float):
    area = side1 * side2
    perimeter = 2 * (side1 + side2)
    return area, perimeter

print(calculateAreaAndPerimeter(2,5))