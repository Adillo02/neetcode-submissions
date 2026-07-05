class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        case = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in case:
                return [case[diff], i ]
            case[num] = i       
        return 