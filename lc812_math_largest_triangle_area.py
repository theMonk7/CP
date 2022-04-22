from decimal import *
from itertools import combinations


class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        ma = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    m = abs(self.__calc_area(points[i], points[j], points[k]))
                    if m > ma:
                        ma = m
        return ma

    def __calc_area(self, p1, p2, p3) -> float:
        getcontext().prec = 5
        return float(Decimal(p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / Decimal(2))

    def largestTriangleArea_with_itertools(self, points: list[list[int]]) -> float:
        ma = 0
        for p1, p2, p3 in combinations(points, 3):
            m = abs(float((p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])) / 2))
            if m > ma:
                ma = m
        return ma

