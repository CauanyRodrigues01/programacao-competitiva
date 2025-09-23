# https://www.geeksforgeeks.org/dsa/count-pairs-a-b-whose-sum-of-cubes-is-n-a3-b3-n/
def pairCubeCount(n):
    soma = 0
    for a in range(1, int(n ** (1/3)) + 1):
        b3 = n - a**3
        b = 0
        while b**3 < b3:  # encontrar um inteiro b tal que b³ = b3, sem usar floats
            b += 1
        if b ** 3 == b3:  # confirma se é cubo perfeito
            soma += 1
    return soma

