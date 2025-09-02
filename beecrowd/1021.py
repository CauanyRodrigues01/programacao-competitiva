"""Leia um valor de ponto flutuante com duas casas decimais. Este
valor representa um valor monetário. A seguir, calcule o menor
número de notas e moedas possíveis no qual o valor pode ser
decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2.
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A
seguir mostre a relação de notas necessárias."""
"""
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    quantNota = int(valor/nota)
    valor -= quantNota * nota
    print(f"{quantNota:.0f} nota(s) de R$ {nota:.2f}")

print("MOEDAS:")
for moeda in moedas:
    quantMoeda = int(round(valor,2)/moeda)
    valor -= round(quantMoeda * moeda, 2)
    print(f"{quantMoeda:.0f} moeda(s) de R$ {moeda:.2f}")
"""
valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
print("NOTAS:")
for nota in notas:
    print(f"{int(valor/nota):.0f} nota(s) de R$ {nota:.2f}")
    valor = float(f"{valor%nota:.2f}")

moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print("MOEDAS:")
for moeda in moedas:
    print(f"{int(valor/moeda):.0f} moeda(s) de R$ {moeda:.2f}")
    valor = float(f"{valor%moeda:.2f}")