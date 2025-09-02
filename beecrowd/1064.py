a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

entradas = [a, b, c, d, e, f]


contPosivos = 0
somaPositivos = 0
for i in entradas:
    if i > 0:
        contPosivos+=1
        somaPositivos+=i
print(f"{contPosivos} valores positivos")
print(f"{somaPositivos/contPosivos:.1f}")