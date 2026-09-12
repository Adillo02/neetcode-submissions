class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Understand: Return indices of Triples that add up to 0 and they cannot be the same
        #Input: Integer Arra
        #Output: nested array with each position being an array with the indices
        #Match: Two pointers

        #Plan:
        #Sort the array
        #Then go through the array and for each number have two pointers starting at the end and beginning
        #if L or R equal move forward or back
        #Check if the sum equals 0 and if that triplet is not in the array 
        #if not in there, then add to the Array
        #return The arrau

        ans = []
        nums.sort()
        for i in range(len(nums)):
            L = i + 1
            R = len(nums) - 1
            if i == 0 or nums[i] != nums[i -1]:
                while L < R:

                    if nums[i] + nums[L] + nums[R] == 0:
                        ans.append([nums[i], nums[L], nums[R]])
                        L += 1
                        while L < R and nums[L] == nums[L - 1]:
                            L += 1
                    elif nums[i] + nums[L] + nums[R] > 0:
                        R -= 1
                    
                    elif nums[i] + nums[L] + nums[R] < 0:
                        L += 1
        
        return ans
        
        

            

                     
                 