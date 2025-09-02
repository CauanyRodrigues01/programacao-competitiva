"""Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o
valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o
valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago."""
peca_1 = input().split() #O método split() tranforma a string em uma lista, sendo cada palavra um item da lista
peca_1 = list(map(float, peca_1)) #O método map() converte as string em números float, depois esses dados são colocados em uma lista com o método list()
peca_2 = input().split()
peca_2 = list(map(float, peca_2))
total = (peca_1[1] * peca_1[2]) + (peca_2[1] * peca_2[2])
print(f"VALOR A PAGAR: R$ {total:.2f}")
