class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxContinuesOne = 0
        tempContinuesOne = 0
        for i in nums:
            if 0 == i:
                maxContinuesOne = max(maxContinuesOne, tempContinuesOne)
                tempContinuesOne = 0
            elif 1 == i:
                tempContinuesOne += 1
        maxContinuesOne = max(maxContinuesOne, tempContinuesOne)
        return maxContinuesOne

sol = Solution()
print(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))