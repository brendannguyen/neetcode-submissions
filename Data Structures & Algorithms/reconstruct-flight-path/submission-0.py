class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dfs
        tickets.sort()
        adjList = {}
        for source, dest in tickets:
            if source not in adjList:
                adjList[source] = []
            adjList[source].append(dest)

        result = ["JFK"]
        def dfs(airport):
            if len(result) == len(tickets)+1:
                return True
            if airport not in adjList:
                return False
            
            temp = list(adjList[airport])
            for i, dest in enumerate(temp):
                adjList[airport].pop(i)
                result.append(dest)
                
                if dfs(dest):
                    return True
                else:
                    adjList[airport].insert(i, dest)
                    result.pop()
            return False

        dfs("JFK")
        return result