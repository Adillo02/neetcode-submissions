class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        list1 = set(nums)
        max_count = 0

        for num in list1:
            count = 1
            if num - 1 in list1:
                track = num - 1
                while track in list1:
                    count += 1
                    track -= 1
            if num + 1 in list1:
                count += 1
            else:
                max_count = max(max_count, count)
        return max_count 
                

        