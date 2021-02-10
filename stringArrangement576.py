class Solution:
    def getStrDict(self, str, index):
        s_dict = dict()
        for i in range(0, index):
            if str[i] in s_dict:
                s_dict[str[i]] += 1
            else:
                s_dict[str[i]] = 1
        return s_dict

    def getDiffDict(self, dict1, dict2):
        diff_dict = dict2.copy()
        for item in dict1:
            if item in diff_dict:
                diff_dict[item] = diff_dict[item] - dict1[item]
            else:
                diff_dict[item] = -dict1[item]
        return diff_dict

    def isDictMatch(self, dict):
        for item in dict:
            if dict[item] != 0:
                return False
        return True

    def moveWindow(self, diff_dict, str, start, end):
        diff_dict[str[start - 1]] -= 1
        if str[end] in diff_dict:
            diff_dict[str[end]] += 1
        else:
            diff_dict[str[end]] = 1
        return self.isDictMatch(diff_dict)


    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        else:
            s1_dict = self.getStrDict(s1, len(s1))
            s2_child_dict = self.getStrDict(s2, len(s1))
            diff_dict = self.getDiffDict(s1_dict, s2_child_dict)
            if self.isDictMatch(diff_dict):
                return True
            start = 0
            end = len(s1) - 1
            while end < len(s2) - 1:
                start += 1
                end += 1
                if self.moveWindow(diff_dict, s2, start, end):
                    return True
            return False


sol = Solution()
print(sol.checkInclusion(s1="ab", s2="eidboaooo"))
