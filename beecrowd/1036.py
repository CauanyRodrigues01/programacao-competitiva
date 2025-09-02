import math

entrada = list(map(float, input().split()))
a, b, c = [num for num in entrada]

if (a==0) or (b==0) or (c==0):
    print("Impossivel calcular")
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Impossivel calcular")
    else:  
        resultado1 = (-b + (math.sqrt(delta)))/(2*a)
        resultado2 = (-b - (math.sqrt(delta)))/(2*a)
        print(f"R1 = {resultado1:.5f}")
        print(f"R2 = {resultado2:.5f}")
