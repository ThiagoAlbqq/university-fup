# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

wage = float(input())
loan = float(input())

if loan > (wage / 5):
    print("Emprestimo não concedido")
else:
    print("Emprestimo concedido")