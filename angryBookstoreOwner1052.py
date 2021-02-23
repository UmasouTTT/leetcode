class Solution(object):
    def calculatePresentMaxSatisfied(self, customrs, grumpy, X, index):
        dropCustomers = index - 1
        addCustomers = index + X - 1
        customersChange = 0
        if 1 == grumpy[dropCustomers]:
            customersChange -= customrs[dropCustomers]
        if 1 == grumpy[addCustomers]:
            customersChange += customrs[addCustomers]
        return customersChange



    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        tempMaxAddSatisfied = 0
        max_start = 0
        result = 0
        for i in range(X):
            if 1 == grumpy[i]:
                tempMaxAddSatisfied += customers[i]
        maxAddSatisfied = tempMaxAddSatisfied
        for i in range(1, len(customers) - X + 1):
            tempMaxAddSatisfied += self.calculatePresentMaxSatisfied(customers, grumpy, X, i)
            if tempMaxAddSatisfied > maxAddSatisfied:
                maxAddSatisfied = tempMaxAddSatisfied
                max_start = i
        for i in range(max_start, max_start + X):
            grumpy[i] = 0
        for i in range(len(customers)):
            if 0 == grumpy[i]:
                result += customers[i]
        return result


sol = Solution()
print(sol.maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3))


