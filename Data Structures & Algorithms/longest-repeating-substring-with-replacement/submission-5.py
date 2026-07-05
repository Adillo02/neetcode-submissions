class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        ans = 0 
       
        char = {} 

        for r in range(len(s)):
            char[s[r]] = 1 + char.get(s[r], 0)
            while (r - L + 1) - max(char.values()) > k:
                char[s[L]] -= 1
                L += 1
            ans = max(ans, r - L + 1)
        return ans       

            
