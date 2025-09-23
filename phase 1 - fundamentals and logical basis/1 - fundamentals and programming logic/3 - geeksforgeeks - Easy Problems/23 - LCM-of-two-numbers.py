# https://www.geeksforgeeks.org/problems/lcm-of-two-numbers/1

# Dividindo o produto dos dois números pelo seu maior divisor comum

import math
def lcm(a, b):
    return (a * b)//math.gcd(a, b)
