# https://www.geeksforgeeks.org/problems/reverse-digit0316/1

'''
# Abordagem 1: Usando Fatiamento de strings
# Time Complexity - O(n)
# Space Complexity - O(n)

class Solution:
	def reverseDigits(self, n):
	    n = str(n)
	    return int(n[::-1])

'''

'''
# Abordagem 2: Interativo
# Time Complexity - O(log n)
# Space Complexity - O(1)

class Solution:
	def reverseDigits(self, n):
		numReverse = ""
		while n > 0:
			numReverse += str(n % 10)
			n = n // 10
		return int(numReverse)
'''
'''
# Método 3: Abordagem recursiva com strings

class Solution:
    def reverseRecursive(self, n):
    	if n == 0:
    		return ""
    	ultimoDigito =  str(n % 10)
    	proximoDigito = str(self.reverseRecusive(n // 10))
    	return ultimoDigito + proximoDigito
    def reverseDigits(self, n):
    	return int(self.reverseRecusive(n))

'''

# Método 4: recursividade usando somente números
# Time Complexity - O(log n)
# Space Complexity - O(log n)

class Solution:
	def reverseRecursive(self, n, revNum, basePos):
		if n > 0:
			self.reverseRecursive(n // 10, revNum, basePos)
			revNum[0] += (n % 10) * basePos[0]
			basePos[0] *= 10

	def reverseDigits(self, n):
		revNum = [0]
		basePos = [1]
		self.reverseRecursive(n, revNum, basePos)
		return revNum[0]