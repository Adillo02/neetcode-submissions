class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         case = set()
         for num in nums:
            if num in case:
                return True 
            if num not in case:
                case.add(num)   
         return False 
        

            

        