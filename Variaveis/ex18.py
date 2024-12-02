saque = int(input())
hundred = saque // 100
fifty = saque % 100 // 50
twenty = saque % 100 % 50 // 20
ten = saque % 100 % 50 % 20 // 10
five = saque % 100 % 50 % 20 % 10 // 5
two = saque % 100 % 50 % 20 % 10 % 5 // 2
one = saque % 100 % 50 % 20 % 10 % 5 % 2
print(hundred, fifty , twenty, ten, five, two, one)
