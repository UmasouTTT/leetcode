class Solution(object):
    def isReshapeLegal(self, nums, r, c):
        if len(nums) * len(nums[0]) == r*c:
            return True
        return False

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not self.isReshapeLegal(nums, r, c):
            return nums
        result = []
        temp = []
        index = 0
        for row in nums:
            for item in row:
                temp.append(item)
                index += 1
                if c == index:
                    result.append(temp.copy())
                    temp.clear()
                    index = 0
        return result


sol = Solution()
print(sol.matrixReshape(nums =
[[1,2],
 [3,4]],
r = 1, c = 4))
