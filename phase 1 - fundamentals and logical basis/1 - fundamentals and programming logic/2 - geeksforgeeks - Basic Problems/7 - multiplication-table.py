# https://www.geeksforgeeks.org/problems/print-table0303/1

'''
Método 1: Abordagem Iterativa

class Solution:
    def getTable(self, n):
        resultados = []
        for i in range(1, 11):
            resultados.append(i * n)
        return resultados
'''

#Método 2: Abordagem Recursiva

class Solution:
    def multiply(self, n, i=1):
        if i > 10:
            return []
        return [n * i] + self.multiply(n, i+1)

    def getTable(self, n):
        return self.multiply(n)
