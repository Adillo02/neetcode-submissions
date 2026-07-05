class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list1 = set(nums)
        max_count = 0

        for i in nums:
            if i - 1 not in list1:
                count = 1
                while (i + count) in list1:
                    count += 1
                max_count = max(count, max_count)

        return max_count 
                

        