entrada = list(map(float, input().split()))
a, b, c = entrada = [num for num in entrada]

if a < b + c and b < a + c and c < a + b:
  perimetro = a+b+c
  print(f"Perimetro = {perimetro:.1f}")
else:
  area_trapezio = ((a+b)*c)/2
  print(f"Area = {area_trapezio:.1f}")
