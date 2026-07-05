class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        count = 0
        

        for i in n:
            if i - 1 not in n:
                length = 1
                while (i + length) in n:
                    length += 1
                count = max(count, length)
        return count 
