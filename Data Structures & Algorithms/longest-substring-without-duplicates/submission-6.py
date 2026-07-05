class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        max_length = 0
        char = set()

        for R in range(len(s)):
            while s[R] in char:
                char.remove(s[L])
                L += 1
            char.add(s[R])
            max_length = max(max_length, R - L + 1)
        return max_length


        
                
        



        