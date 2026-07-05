class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for index, value in enumerate(nums):
            diff = target - value

            if diff in table:
                return [table[diff], index]
            
            table[value] = index
        