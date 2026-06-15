class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # traverse via dfs until end, adding to output, but if cycle is detected, return []\
        preReqMap = {}
        for i in range(numCourses):
            preReqMap[i] = []
        
        for course, preReq in prerequisites:
            preReqMap[course].append(preReq)

        output = []
        cycle = set()
        visited = set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for preReq in preReqMap[course]:
                if dfs(preReq) == False:
                    return False

            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        
        return output
