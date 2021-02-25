class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        transposeMatrix = []
        for column in range(len(matrix[0])):
            transposeMatrix.append([])
            for row in range(len(matrix)):
                transposeMatrix[column].append(matrix[row][column])
        return transposeMatrix

sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6]]))


