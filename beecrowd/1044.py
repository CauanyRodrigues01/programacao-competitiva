entrada = list(map(int, input().split()))
a, b = [num for num in entrada]

if a%b == 0 or b%a == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")
