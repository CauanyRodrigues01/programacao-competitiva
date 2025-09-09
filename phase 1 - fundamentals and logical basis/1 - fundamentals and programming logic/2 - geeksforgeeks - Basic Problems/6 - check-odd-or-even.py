# https://www.geeksforgeeks.org/problems/odd-or-even3618/1

'''
Método 1:

class Solution:
    def isEven (self, n):
        return n % 2 == 0
'''

# Método 2: Usando o Operador AND Bitwise
class Solution:
    def isEven (self, n):
        return n & 1 == 0