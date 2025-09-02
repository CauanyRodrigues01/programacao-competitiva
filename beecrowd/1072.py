quant = int(input())

contDentro = 0
contFora = 0
for i in range(quant):
    num = int(input())
    if num >= 10 and num <= 20:
        contDentro += 1
    else:
        contFora += 1

print(contDentro,"in")
print(contFora,"out")