# Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário então imprima: "Emprestimo nao concedido", caso contrário imprima: "Emprestimo concedido".

wage = float(input())
loan = float(input())

print("Emprestimo não concedido" if loan > (wage / 5) else "Emprestimo concedido")