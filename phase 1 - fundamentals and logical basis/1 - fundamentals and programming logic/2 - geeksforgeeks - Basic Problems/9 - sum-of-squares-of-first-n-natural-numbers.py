# https://www.geeksforgeeks.org/problems/sum-of-squares-of-first-n-natural-numbers/1

'''
Método 1: Abordagem Iterativa

class Solution:

    def sumOfSquares(self, number):
        return sum( i**2 for i in range(1, number+1) )
'''

# Método 2: Abordagem usando a Fórmula da soma de números quadrados perfeitos consecutivos

# Fórmula: n * (n + 1) * (2n + 1) / 6
# Divisão da primeira parte por 2 e da segunda por 3 para reduzir o tamanho e evitar estouro

class Solution:

    def sumOfSquares(self, n):
        return (n * (n + 1) // 2) * (2 * n + 1) // 3