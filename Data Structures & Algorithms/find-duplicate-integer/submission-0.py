class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        past_numbers = set()

        for num in nums:
            if num in past_numbers:
                return num
            else:
                past_numbers.add(num)



        