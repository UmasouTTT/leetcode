class Solution(object):
    def isCouple(self, row, index):
        if abs(row[index] - row[index + 1]) == 1:
            if min(row[index], row[index + 1]) % 2 == 0:
                return True
        return False


    def findCouple(self, num):
        if num % 2 == 0:
            return num + 1
        else:
            return num - 1

    def swap(self, row, index1, index2):
        temp = row[index1]
        row[index1] = row[index2]
        row[index2] = temp

    def findSuitablePosition(self, row, index, other_part):
        for i in range(index + 1, len(row)):
            if row[i] == other_part:
                self.swap(row, index, i)
                return

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        times = 0
        for i in range(0, len(row), 2):
            if not self.isCouple(row, i):
                self.findSuitablePosition(row, i + 1, self.findCouple(row[i]))
                times += 1
        return times

sol = Solution()
print(sol.minSwapsCouples([3, 2, 0, 1]))
