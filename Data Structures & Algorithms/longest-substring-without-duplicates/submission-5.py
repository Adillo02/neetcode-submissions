class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, R  = 0, 0
        max_length = 0
        char = set()

        for r in range(len(s)):
            while s[r] in char:
                char.remove(s[L])
                L += 1
            char.add(s[R])
            R += 1
            max_length = max(max_length, R - L )
        return max_length


        
                
        



        