# 9. Crie uma função que, dada uma velocidade em km/h (quilômetros por hora) e retorne-a convertida em m/s (metros por segundo). 
# A fórmula de conversão é: M = K/3.6 , sendo K a velocidade em km/h e M em m/s.

def kilometersPerHourToMetersPerSeconds(km: float):
    return km/3.6

print(kilometersPerHourToMetersPerSeconds(72))