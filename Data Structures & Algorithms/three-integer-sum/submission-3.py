class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, value in enumerate(nums):
            if i > 0 and value == nums[i -1]:
                continue
            
            L, R= i + 1, len(nums) - 1

            while L < R:
                target = nums[L] + nums[R] + value

                if target == 0:
                    ans.append([value, nums[L], nums[R]])
                    L += 1
                    while L < len(nums) and nums[L - 1] == nums[L]:
                        L += 1
                elif target > 0:
                    R -= 1
                elif target < 0:
                    L += 1
        return ans 



        


            

                     
                 