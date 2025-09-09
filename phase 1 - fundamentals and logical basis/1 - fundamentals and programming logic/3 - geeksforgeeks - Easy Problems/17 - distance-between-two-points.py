# https://www.geeksforgeeks.org/problems/distance-between-2-points3200/1

import math

class Solution:
    def distance(self, x1, y1, x2, y2):
        dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        return round(dist)