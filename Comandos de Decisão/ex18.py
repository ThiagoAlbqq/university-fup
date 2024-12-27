# Faça um função que receba a data atual (cadeia de caracteres no formato “DD/MM/AAAA”) e retorne uma string com a data onde o mês está no formato textual por extenso. Considere que a data é válida. Exemplo: Data: 01/01/2000, retornar: 1 de janeiro de 2000.

date = str(input())
split = date.split("/")

mes = "janeiro"

if int(split[1]) == 1: mes = "janeiro"
if int(split[1]) == 2: mes = "fevereiro"
if int(split[1]) == 3: mes = "marco"
if int(split[1]) == 4: mes = "abril"
if int(split[1]) == 5: mes = "maio"
if int(split[1]) == 6: mes = "junho"
if int(split[1]) == 7: mes = "julho"
if int(split[1]) == 8: mes = "agosto"
if int(split[1]) == 9: mes = "setembro"
if int(split[1]) == 10: mes = "outubro"
if int(split[1]) == 11: mes = "novembro"
if int(split[1]) == 12: mes = "dezembro"

print(f'{split[0]} de {mes} de {split[2]}')