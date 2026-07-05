class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        case = {}
        for chr in s:
            if chr in case:
                case[chr] += 1
            else:
                case[chr] = 1
        case1 = {}
        for chr1 in t:
            if chr1 in case1:
                case1[chr1] += 1
            else:
                case1[chr1] = 1
        if case == case1: 
            return True 
        return False 