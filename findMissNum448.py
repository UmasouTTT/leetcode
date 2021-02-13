#官方思路:数组中每个数哈希到对应位置，然后该索引对应位置值+len(nums)
#之后数组中值<len(nums)的数表示该索引不在数组中
#核心思想：索引代替数
class Solution:

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        result = []
        max = nums[0]
        for i in range(1, max):
            result.append(i)
        for i in range(0, len(nums)):
            if nums[i] != max:
                if nums[i] - max > 1:
                    for j in range(max + 1, nums[i]):
                        result.append(j)
                max = nums[i]
        for i in range(max + 1, len(nums) + 1):
            result.append(i)
        return result


sol = Solution()
a = [1, 1]
print(sol.findDisappearedNumbers(a))



