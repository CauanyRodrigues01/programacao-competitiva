# https://www.geeksforgeeks.org/problems/factorial5739/1

class Solution:
    def factorial(self, n: int) -> int:
        return self.recursive(n)

    def recursive(self, n):
        if n == 0:
            return 1
        return n * self.recursive(n - 1)