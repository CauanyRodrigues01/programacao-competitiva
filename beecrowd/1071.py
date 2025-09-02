num1 = int(input())
num2 = int(input())

def trocaValor(num1, num2):
    aux = 0
    if num1 > num2:
        aux = num1
        num1 = num2
        num2 = aux
    return num1, num2

num1, num2 = trocaValor(num1, num2)

soma = 0
for i in range(num1+1, num2):
    if (i % 2) != 0:
        soma += i
print(soma)
