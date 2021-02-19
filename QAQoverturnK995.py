# class Solution(object):
#     def findFirstZero(self, A, index):
#         for i in range(index, len(A)):
#             if 0 == A[i]:
#                 return i
#         return -1
#
#     def FlipKNumFromIndex(self, A, K, index):
#         if (len(A) - index) < K:
#             return -1
#         nextIndex = index + K
#         for i in range(index, index + K):
#             if 1 == A[i]:
#                 A[i] = 0
#                 nextIndex = min(nextIndex, i)
#             else:
#                 A[i] = 1
#         return nextIndex
#
#
#     def minKBitFlips(self, A, K):
#         """
#         :type A: List[int]
#         :type K: int
#         :rtype: int
#         """
#         index = 0
#         step = 0
#         while index < len(A):
#             index = self.findFirstZero(A, index)
#             if -1 == index:
#                 return step
#             index = self.FlipKNumFromIndex(A, K, index)
#             if -1 == index:
#                 return -1
#             step += 1
#         return step

class Solution(object):
    def isPresentZero(self, A, index, revTime, diff):
        revTime = revTime + diff[index]
        if 0 == revTime % 2 and 0 == A[index]:
            return True
        if 1 == revTime % 2 and 1 == A[index]:
            return True
        return False

    def revOnce(self, diff, index, K):
        if (len(diff) - index) < K:
            return -1
        diff[index] += 1
        if index + K <= len(diff) - 1:
            diff[index + K] -= 1


    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        diff = [0 for i in A]
        revTime = 0
        wholeRevTime = 0
        for i in range(0, len(A)):
            if self.isPresentZero(A, i, revTime, diff):
                if -1 == self.revOnce(diff, i, K):
                    return -1
                wholeRevTime += 1
            revTime += diff[i]
        return wholeRevTime




sol = Solution()
print(sol.minKBitFlips(A = [0,0,0,1,0,1,1,0], K = 3))