"""Faça um programa que leia três valores e apresente o maior dos três valores
lidos seguido da mensagem “eh o maior”. Utilize a fórmula:
Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b).
Um segundo passo, portanto é necessário para chegar no resultado esperado."""

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
maiorAB = (a+b+abs(a-b))/2
maiorDeTodos = (maiorAB+c+abs(maiorAB-c))/2
print(f"{maiorDeTodos:.0f} eh o maior")
