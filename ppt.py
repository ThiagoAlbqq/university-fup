import random
jogadas = []
types = {
    "1": "PEDRA",
    "2": "PAPEL",
    "3": "TESOURA"
}

while True: 
    escolha_do_computador = random.randint(1,3)
    print("----------JOKENPO----------")
    print("""
    [ 1 ] Pedra
    [ 2 ] Papel
    [ 3 ] Tesoura
    [ 4 ] Historico
    """)
    escolha = int(input())
    if escolha not in (1,2,3,4):
        print("Houve um erro de digitação...")
        continue

    if escolha==4:
        print("HISTORICO:")
        for jogada in jogadas:
            print(f'O jogador escolheu {types[str(jogada["escolha"])]}, o computador {types[str(jogada["computador"])]}, resultado {jogada["resultado"]}')
        continue
    elif ((escolha==1 and escolha_do_computador==1) or (escolha==2 and escolha_do_computador==2) or (escolha==3 and escolha_do_computador==3)):
        print("EMPATE!")
        resultado = "EMPATE"
    elif ((escolha==1 and escolha_do_computador==3) or (escolha==2 and escolha_do_computador==1) or (escolha==3 and escolha_do_computador==2)):
        print("GANHOU!")
        resultado = "GANHOU"
    elif ((escolha==1 and escolha_do_computador==2) or (escolha==2 and escolha_do_computador==3) or (escolha==3 and escolha_do_computador==1)):
        print("PERDEU!")
        resultado = "PERDEU"

    jogada = {
        "escolha": escolha,
        "computador": escolha_do_computador,
        "resultado": resultado 
    }

    jogadas.append(jogada)

    continuar = input("Continuar? (s/n)").lower()
    if continuar=="n":
        break