# https://www.geeksforgeeks.org/problems/closest-number5728/1

'''
Método 1: Usando arredondamento (round) e verificação entre candidatos
class Solution:
    def closestNumber(self, n, m):

        multiplo_proximo = round(n / m) * m
        multiplo_anterior = multiplo_proximo - m
        multiplo_posterior = multiplo_proximo + m

        candidatos = [multiplo_anterior, multiplo_proximo, multiplo_posterior]

        mais_proximo = candidatos[0]
        for x in candidatos:
            if abs(n - x) < abs(n - mais_proximo):
                mais_proximo = x
            elif abs(n - x) == abs(n - mais_proximo):
                if abs(x) > abs(mais_proximo):
                    mais_proximo = x

        return mais_proximo
'''

#Método 2: Usando divisão inteira e comparação direta
class Solution:
    def closestNumber(self, n, m):

        quociente = n // m
        multiplo_mais_proximo_abaixo = m * quociente

        if n * m > 0:
            multiplo_mais_proximo_acima = m * (quociente + 1)
        else:
            multiplo_mais_proximo_acima = m * (quociente - 1)

        # Comparar distâncias e retornar o mais próximo
        if abs(n - multiplo_mais_proximo_abaixo) < abs(n - multiplo_mais_proximo_acima):
            return multiplo_mais_proximo_abaixo
        elif abs(n - multiplo_mais_proximo_abaixo) > abs(n - multiplo_mais_proximo_acima):
            return multiplo_mais_proximo_acima
        else:
            # Se empate, escolher o de maior valor absoluto
            return multiplo_mais_proximo_abaixo if abs(multiplo_mais_proximo_abaixo) >= abs(
                multiplo_mais_proximo_acima) else multiplo_mais_proximo_acima
