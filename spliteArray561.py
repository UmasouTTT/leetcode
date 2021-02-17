class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                result += nums[i]
        return result


