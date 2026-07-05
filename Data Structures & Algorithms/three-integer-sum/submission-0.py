class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        ans = []

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i -1]:
                continue
            L, R = i + 1, len(nums) - 1
            while L < R:
                if a + nums[L] + nums[R] > 0:
                    R -= 1
                elif a + nums[L] + nums[R] < 0:
                    L += 1
                else:
                    ans.append([a, nums[L], nums[R]])
                    L += 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1

        return ans


                 