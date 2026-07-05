class Solution:
    def isPalindrome(self, s: str) -> bool:
        New_s = []
        for chr in s:
            if chr.isalnum():
                New_s.append(chr.lower())
        L = 0
        R = len(New_s) - 1
        

        while L < R:
            if New_s[L] != New_s[R]:
                return False
            L += 1
            R -= 1
        return True 
        