# https://www.geeksforgeeks.org/problems/check-if-a-number-is-power-of-another-number5442/1

import math
class Solution:
    def isPowerOfAnother(self, X, Y):

        if X <= 0 or Y <= 0:
            return False
        if X == 1:
            return Y == 1
        if Y == 1:
            return True

        log = math.log(Y, X)

        return log.is_integer()