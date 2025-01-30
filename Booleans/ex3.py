nome = input()
letra = input()
novoNome = ""
vogais = 0

for char in nome:
    if char in "AaEeIiOoUu":
        vogais += 1
        novoNome += letra
    else:
        novoNome += char
    

print(vogais)
print(novoNome)