"""Leia um valor inteiro. A seguir, calcule o menor número de
notas possíveis (cédulas) no qual o valor pode ser decomposto.
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir
mostre o valor lido e a relação de notas necessárias."""

valor = int(input())

quantCem = int(valor/100)
resto = valor - quantCem*100
quantCinquenta = int(resto/50)
resto -= quantCinquenta * 50
quantVinte = int(resto/20)
resto -= quantVinte * 20
quantDez = int(resto/10)
resto -= quantDez * 10
quantCinco = int(resto/5)
resto -= quantCinco * 5
quantDois = int(resto/2)
resto -= quantDois * 2
quantUm = int(resto/1)

print(valor)
print(f"{quantCem} nota(s) de R$ 100,00")
print(f"{quantCinquenta} nota(s) de R$ 50,00")
print(f"{quantVinte} nota(s) de R$ 20,00")
print(f"{quantDez} nota(s) de R$ 10,00")
print(f"{quantCinco} nota(s) de R$ 5,00")
print(f"{quantDois} nota(s) de R$ 2,00")
print(f"{quantUm} nota(s) de R$ 1,00")
