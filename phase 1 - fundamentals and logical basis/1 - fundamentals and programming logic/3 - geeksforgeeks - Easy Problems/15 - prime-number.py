# https://www.geeksforgeeks.org/problems/prime-number2314/1

# Princípio da raiz quadrada: Se um número n não tem divisores menores ou iguais à sua raiz quadrada, então não terá
# nenhum divisor maior que a raiz, exceto ele mesmo.
# Todo número primo maior que 3 está próximo de múltiplos de 6, ou seja, é da forma: 6k−1 ou 6k+1

import math
class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
                return False

        # Começa pelo 5 que é o menor número da forma 6k - 1
        # O loop vai no passo 6 para pegar todos os número 6k - 1
        for i in range(5, int(math.sqrt(n))+1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True
