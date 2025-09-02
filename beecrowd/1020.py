"""Leia um valor inteiro correspondente à idade de uma pessoa em
dias e informe-a em anos, meses e dias"""

dias = int(input())
anos = int(dias/365)
resto = dias - anos*365
meses = int(resto/30)
resto -= meses*30
dias = resto
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
