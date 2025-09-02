entrada = list(map(float, input().split()))
entrada.sort(reverse=True)

a, b, c = [num for num in entrada]

tipo = []
if a >= (b+c):
  tipo.append("NAO FORMA TRIANGULO")
else:
  if a**2 == (b**2 + c**2):
    tipo.append("TRIANGULO RETANGULO")
  if a**2 > (b**2 + c**2):
    tipo.append("TRIANGULO OBTUSANGULO")
  if a**2 < (b**2 + c**2):
    tipo.append("TRIANGULO ACUTANGULO")
  if a == b == c:
    tipo.append("TRIANGULO EQUILATERO")
  if (a == b and b != c) or (b == c and c != a) or (c == a and a != c):
    tipo.append("TRIANGULO ISOSCELES")

for i in tipo:
  print(i)
