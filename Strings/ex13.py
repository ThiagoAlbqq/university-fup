# 13.  Faça uma função que receba um valor em R$ que será dividido entre três ganhadores de um 
# concurso. Sendo que da quantia total:
# ◦ O primeiro ganhador receberá 46%;
# ◦ O segundo ganhador receberá 32%;
# ◦ O terceiro receberá o restante;
# Calcule e retorne a quantia ganha por cada um dos ganhadores.

def calculateDivisionOfAward(award: float):
    return award * 0.46, award * 0.32, award * 0.22

print(calculateDivisionOfAward(100))