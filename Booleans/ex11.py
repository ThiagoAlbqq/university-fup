def funcao(data):
    if len(data) != 10:
        return 0, 0, 0
    

    if data[2] != '/' or data[5] != '/':
        return 0, 0, 0
    

    dia, mes, ano = data.split('/')
    

    if not (dia.isdigit() and mes.isdigit() and ano.isdigit()):
        return 0, 0, 0
    

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    

    if not (1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0):
        return 0, 0, 0

    return dia, mes, ano
