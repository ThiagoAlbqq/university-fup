nome = input()
novoNome = ""

for char in nome:
    if char not in "AaEeIiOoUu":
        novoNome += char

print(novoNome)
