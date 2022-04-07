class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary.sort()
        sum = 0
        cnt = 0
        for i in range(1, len(salary) - 1):
            sum += salary[i]
            cnt += 1
        return float("{:.5f}".format(sum / cnt))

print(Solution().average([48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]))