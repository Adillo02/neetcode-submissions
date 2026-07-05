class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        L = 0
        R = len(numbers) - 1
        curr_sum = 0
       
        while L < R:
            curr_sum = numbers[L] + numbers[R]
            if curr_sum < target:
                L += 1
            elif curr_sum > target:
                R -= 1
            else:
                ans.append(L + 1)
                ans.append(R + 1)
                return ans 



        