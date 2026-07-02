class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        


        for i, value in enumerate(nums):
            if i > 0 and value == nums[i - 1]:
                continue
            
            L, R = i + 1, len(nums) -1

            while L < R:
                if nums[L] + nums[R] + value == 0:
                    res.append([value, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L -1] and L < R:
                        L += 1
                elif nums[L] + nums[R] + value > 0 :
                    R -= 1
                else:
                    L += 1

            
           
        return res
            

            

                     
                 