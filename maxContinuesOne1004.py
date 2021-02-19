# 0变1 1变0，求和后可以迅速得到0的个数
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxlength = 0
        tempMaxLength = 0
        tempK = K
        tempStart = 0
        for i in range(len(A)):
            if 0 == A[i]:
                if 0 == K:
                    maxlength = max(maxlength, tempMaxLength)
                    tempMaxLength = 0
                    continue
                if 0 == tempK:
                    maxlength = max(maxlength, tempMaxLength)
                    for j in range(tempStart, i):
                        tempMaxLength -= 1
                        if 0 == A[j]:
                            tempStart = j + 1
                            break
                else:
                    tempK -= 1
            tempMaxLength += 1
        maxlength = max(maxlength, tempMaxLength)
        return maxlength


sol = Solution()
print(sol.longestOnes(A = [0,0,1,1,1,0,0], K = 0))





