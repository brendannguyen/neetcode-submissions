class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's algorithm (euclerian path)
        # O(ElogE)
        # iterative
        adjList = {}
        for source, dest in sorted(tickets, reverse=True):
            if source not in adjList:
                adjList[source] = []
            if dest not in adjList:
                adjList[dest] = []
            adjList[source].append(dest)

        stack = ["JFK"]
        result = []

        while stack:
            curr = stack[-1]
            if not adjList[curr]:
                result.append(stack.pop())
            else:
                stack.append(adjList[curr].pop())
        
        return result[::-1]