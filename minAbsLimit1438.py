class Solution(object):
    def smallerStartSatisfyLimit(self, start, end, nums, limit):
        result = end
        largestNum = nums[end]
        for i in range(end, start - 1, -1):
            if nums[i] - nums[end] > limit:
                break
            largestNum = max(largestNum, nums[i])
            result = i
        return result, largestNum

    def largerStartSatisfyLimit(self, start, end, nums, limit):
        result = end
        minNum = nums[end]
        for i in range(end, start - 1, -1):
            if nums[end] - nums[i] > limit:
                break
            minNum = min(minNum, nums[i])
            result = i
        return result, minNum



    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        min_num = nums[0]
        max_num = nums[0]
        best_start = 0
        best_end = 0
        start = 0
        end = 0
        maxChildArrayLength = 0
        for i in range(0, len(nums)):
            if min_num > nums[i]:
                min_num = nums[i]
                if max_num - min_num > limit:
                    start, max_num = self.smallerStartSatisfyLimit(start, i, nums, limit)
            elif max_num < nums[i]:
                max_num = nums[i]
                if max_num - min_num > limit:
                    start, min_num = self.largerStartSatisfyLimit(start, i, nums, limit)
            end = i
            maxChildArrayLength = max(maxChildArrayLength, end - start + 1)
        return maxChildArrayLength

sol = Solution()
print(sol.longestSubarray([7,40,10,10,40,39,96,21,54,73,33,17,2,72,5,76,28,73,59,22,100,91,80,66,5,49,26,45,13,27,74,87,56,76,25,64,14,86,50,38,65,64,3,42,79,52,37,3,21,26,42,73,18,44,55,28,35,87],63))