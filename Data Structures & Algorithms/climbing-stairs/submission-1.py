class Solution:
    def climbStairs(self, n: int) -> int:
        #Understand: n represents how many staircases there are to climb and we want to find out the many different ways of doing it

        #Input: An integer
        #Output: number of possibilities

        #Match:Dynamic Programming fibonacci

        #Plan use the previous two positions to determine the amount of c=outcomes for each position.
        #Use one and Two two store the previous two pposibillities since we wither take only one step or 2.
        #There is no need to repeat steps.


        one, two = 1, 1

        for i in range(n -1):
            temp = one
            one = one + two
            two = temp
        
        return one
        


        

        