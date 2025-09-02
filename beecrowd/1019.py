"""Leia um valor inteiro, que é o tempo de duração em segundos de
um determinado evento em uma fábrica, e informe-o expresso no
formato horas:minutos:segundos."""

totalSegundos = int(input())

totalMinutos = int(totalSegundos/60)
segundos = totalSegundos - (totalMinutos*60)
horas = int(totalMinutos/60)
minutos = totalMinutos - (horas*60)

print(f"{horas}:{minutos}:{segundos}")
