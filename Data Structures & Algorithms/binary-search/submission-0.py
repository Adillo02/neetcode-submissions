class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            index = (L + R) // 2

            if nums[index] == target:
                return index
            
            elif nums[index] > target:
                R = index - 1
            
            elif nums[index] < target:
                L = index + 1

        return -1
                
        