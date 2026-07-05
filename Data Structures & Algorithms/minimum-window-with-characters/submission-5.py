class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        elif t == s:
            return t
        
        key, char = {}, {}
        
        for i in t:
            key[i] = 1 + key.get(i, 0)
        
        have, need = 0, len(key)
        L = 0
        ans, length = [0,0], float("infinity") 

        for r in range(len(s)):
            a = s[r]
            char[a] = 1 + char.get(a, 0)

            if a in key and char[a] == key[a]:
                have += 1
            while have == need:
                if (r - L + 1) < length:
                    ans = [L, r]
                    length = r - L + 1
                char[s[L]] -= 1
                if s[L] in key and char[s[L]] < key[s[L]]:
                    have -= 1
                L += 1
        L, r = ans

        return s[L:r + 1] if length != float("infinity") else ""
                






         
        