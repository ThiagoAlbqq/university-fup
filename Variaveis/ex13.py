num = int(input())
c = num // 100
d = num % 100 // 10
u = num % 100 % 10
print(u * 100 + d * 10 + c)