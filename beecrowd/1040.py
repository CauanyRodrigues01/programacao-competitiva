entrada = list(map(float, input().split()))
n1, n2, n3, n4 = [num for num in entrada]

media = (n1*2 + n2*3 + n3*4 + n4)/10
print(f"Media: {media:.1f}")

if media >= 7:
  print("Aluno aprovado.")
elif media < 5:
  print("Aluno reprovado.")
elif 5 <= media <= 6.9:
  print("Aluno em exame.")
  
  exame = float(input())
  print(f"Nota do exame: {exame:.1f}")

  media_final = (media+exame)/2

  if media_final >= 5:
    print("Aluno aprovado.")
  elif media_final < 5:
    print("Aluno reprovado.")
  print(f"Media final: {media_final:.1f}")
