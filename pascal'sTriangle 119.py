class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        result = [1, 1]
        for i in range(1, rowIndex):
            result = [result[i] + result[i + 1] for i in range(0, len(result) - 1)]
            result.insert(0, 1)
            result.append(1)
        return result

sol = Solution()
print(sol.getRow(3))
