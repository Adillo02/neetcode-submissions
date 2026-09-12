class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""

        for char in s:
            if char.isalnum():
                clean += char.lower()
        
        L, R = 0, len(clean) - 1

        while L <= R:
            if clean[R] != clean[L]:
                return False
            
            L += 1
            R-= 1
        return True
                