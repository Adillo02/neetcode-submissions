class Solution:
    def hammingWeight(self, n: int) -> int:
        number = n

        count = 0

        while number:
            count += number % 2
            number = number >> 1

        return count 

        