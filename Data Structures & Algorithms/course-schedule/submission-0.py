class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #Understand: we muct determine if its possible to take all courses

        #Input: number of courses, nested array that shows course and its prerequisite
        #Output: true or false if its possible

        #Match : DFS since we are trying to detect a cycle

        #Plan: Use a hashmap to store courses and its prereqiuistes
        #Loop tthrough the array again and call DFS for each course
        #Have a set to know which course we have already visited and if we already visited a course in a path we would return False
        #Base Case: If the preques have already been visite/done we return True 
        #Otherwise we mark the course as visited and call DFS for  the prerequisit. After we remove it from visit because the we are done with the course
        #And at the end verify every course and orereq is True


        freq = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            freq[crs].append(pre)


        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if freq[crs] == []:
                return True
            
            visited.add(crs)
            for pre in freq[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            freq[crs] = []
            return True
        for crs, pre in prerequisites:
            if not dfs(crs):
                return False
        
        return True 




        
        