class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        L = 0
        char = {}
        key = {} 

        for i in range(len(s1)):
            if s1[i] in key:
                key[s1[i]] += 1
            else:
                key[s1[i]] = 1
        for r in range(len(s2)):
            if s2[r] in char:
                char[s2[r]] += 1
            else:
                char[s2[r]] = 1

            if (r - L + 1) > len(s1):
                char[s2[L]] -= 1
                if char[s2[L]] == 0:
                    del char[s2[L]]
                L += 1

            if char == key:
                return True
        return False 

        
        
