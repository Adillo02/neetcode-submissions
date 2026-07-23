class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        curr = n

        while curr != 1 and curr not in seen:
            seen.add(curr)
            total = 0

            while curr > 0:
                digit = curr % 10
                total += digit * digit
                curr = curr // 10
            curr = total
            

        
        if curr == 1:
            return True
        else:
            return False 
            

        