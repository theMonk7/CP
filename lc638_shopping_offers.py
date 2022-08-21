class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:

        return self.__help(needs, price, special, 0, 0)

    def __help(self, need, price, spcl, i, o):
        if i == len(need):
            return 0

        take_off = 1000000000000000000000
        cost = need[i] * price[i]
        ne = need[i]
        need[i] = 0
        take_no_off = cost + self.__help(need[:], price, spcl, i + 1, o)
        need[i] = ne

        valid = True
        for k in range(o, len(spcl)):
            for j in range(len(spcl[k][:-1])):
                if spcl[k][j] > need[j]:
                    valid = False
            if valid:
                for t in range(len(need)):
                    need[t] -= spcl[k][t]
                take_off = spcl[k][-1] + self.__help(need, price, spcl, i + 1, k)
        return min(take_off, take_no_off)

print(Solution().shoppingOffers([2,5],[[3,0,5],[1,2,10]],[3,2]))