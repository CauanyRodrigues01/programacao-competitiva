# https://www.geeksforgeeks.org/problems/sum-of-series2811/1

'''
Método 1: Abordagem Iterativa

class Solution:
    def findSum(self, n):
        soma = 0
        for i in range(1, n + 1):
            soma += i
        return soma
'''

'''
Método 2: Abordagem Recursiva

class Solution:
    def recursiveSum(self, n, i=0):
        if i > n:
            return 0
        return i + self.recursiveSum(n, i + 1)
    def findSum(self, n):
        return self.recursiveSum(n)
'''

# Método 3: Abordagem baseado em fórmulas

# Usando a fórmula de PA
class Solution:
    def findSum(self, n):
        return (n * (n + 1)) // 2