class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []

        L, R = 0, len(numbers) - 1

        while L < R:
            sum_ans = numbers[L] + numbers[R]

            if sum_ans == target:
                return [L + 1, R + 1]
            elif sum_ans > target:
                R -= 1
            elif sum_ans < target:
                L += 1
        
        



        