class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        preReqMap = {}
        
        for course, preReq in prerequisites:
            preReqMap.setdefault(course, []).append(preReq)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            
            if course not in preReqMap:
                return True
            
            visited.add(course)
            for preReq in preReqMap[course]:
                if dfs(preReq) == False:
                    return False
            visited.remove(course)
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

