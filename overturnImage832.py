class Solution(object):
    def overturnLine(self, line):
        for i in range(int((len(line) + 1) / 2)):
            temp = line[i]
            line[i] = line[len(line) - i - 1]
            line[len(line) - i - 1] = temp

    def inverseLine(self, line):
        for i in range(len(line)):
            if 0 == line[i]:
                line[i] = 1
            else:
                line[i] = 0

    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for line in A:
            self.overturnLine(line)
            self.inverseLine(line)
        return A

sol = Solution()
print(sol.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))
