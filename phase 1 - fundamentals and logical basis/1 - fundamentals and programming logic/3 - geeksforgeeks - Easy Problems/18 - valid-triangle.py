# https://www.geeksforgeeks.org/problems/valid-triangle--121441/1

# Os três lados formam um triângulo se, e somente se, a soma de quaisquer dois lados for maior que o terceiro

class Solution:
    def checkValidity(self, a: int, b: int, c: int) -> bool:
        return (a + b) > c and (b + c) > a and (c + a) > b
