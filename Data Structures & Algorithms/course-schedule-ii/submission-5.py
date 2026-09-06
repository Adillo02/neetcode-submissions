class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #Understand: We want to return an order of classes we take to finish them all
        #Input: an array of courses paired with the prereuisites
        #output: An array showing an order of completing all classes

        #Match: DFS treat the array as a graph

        #Plan: Use a hasdmap to store a course and it's prerequisites
        #Call DFS to dteremine a path to complete all courses 
        #Base case: if course is already in the set/path return []
        #base case: if course has no prerequisites add it to the order return nothing
        #Else call DFS on all prerequisites and see

        schedule = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            schedule[crs].append(pre)

        ans = []
        visited = set()
        processed = set()
        def dfs(crs):

            if crs in visited:
                return False
            if crs in processed:
                return True
                           
            visited.add(crs)
            for pre in schedule[crs]:
                if not dfs(pre):
                    return False
            
            processed.add(crs)

            ans.append(crs)

            visited.remove(crs)
            
            return True

            
        for crs in schedule:
            if not dfs(crs):
                return []
        
        return ans
