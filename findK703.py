class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        if k > len(nums):
            self.nums_set = nums
            self.nums_set.sort(reverse=True)
        else:
            self.nums_set = nums
            self.nums_set.sort(reverse=True)
            self.nums_set = [self.nums_set[i] for i in range(0, self.k)]





    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums_set) < self.k:
            for i in range(0, len(self.nums_set)):
                if val > self.nums_set[i]:
                    self.nums_set.insert(i, val)
                    break
            self.nums_set.append(val)
        else:
            for i in range(0, self.k):
                if val > self.nums_set[i]:
                    self.nums_set.insert(i, val)
                    self.nums_set.pop()
                    break
        print(self.nums_set)
        if len(self.nums_set) < self.k:
            return None
        return self.nums_set[self.k - 1]


list = [[3],[2],[3],[1],[2],[4],[5],[5],[6],[7],[7],[8],[2],[3],[1],[1],[1],[10],[11],[5],[6],[2],[4],[7],[8],[5],[6]]
kthLargest = KthLargest(7,[-10,1,3,1,4,10,3,9,4,5,1])
for _list in list:
    print(kthLargest.add(_list[0]))



