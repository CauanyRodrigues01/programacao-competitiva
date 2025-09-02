entrada = list(map(int, input().split()))
cod, quant = [num for num in entrada]
if cod == 1:
  valor = 4
elif cod == 2:
  valor = 4.5
elif cod == 3:
  valor = 5
elif cod == 4:
  valor = 2
elif cod == 5:
  valor = 1.5
print(f"Total: R$ {(quant*valor):.2f}")
