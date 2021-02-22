class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            compare = matrix[i][0]
            for j in range(1, min(len(matrix) - i, len(matrix[0]))):
                print ((i, 0), (i+j, j))
                if compare != matrix[i + j][j]:
                    return False
        for i in range(1, len(matrix[0])):
            compare = matrix[0][i]
            for j in range(1, min(len(matrix), len(matrix[0]) - i)):
                print ((0, i), (j, i + j))
                if compare != matrix[j][i + j]:
                    return False
        return True

sol = Solution()
print(sol.isToeplitzMatrix(matrix = [[11,74,0,93],[40,11,74,7]]))