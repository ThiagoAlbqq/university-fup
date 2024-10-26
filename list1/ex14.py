num = int(input())
m = num // 1000
c = num % 1000 // 100
d = num % 1000 % 100 // 10
u = num % 1000 % 100 % 10
print(m)
print(c)
print(d)
print(u)