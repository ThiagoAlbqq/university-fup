# 16. Faça uma função que receba um valor inteiro positivo em segundos, e retorne-o em horas, minutos e segundos.

def convertSecondsToTime(sec: int):
    hours = sec // 360
    minutes = sec % 360 // 60
    seconds = sec % 360 % 60
    return hours, minutes, seconds

print(convertSecondsToTime(421))