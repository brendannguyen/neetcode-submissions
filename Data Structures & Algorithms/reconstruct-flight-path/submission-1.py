class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Hierholzer's algorithm (euclerian path)
        # O(ElogE)

        adjList = {}
        for source, dest in sorted(tickets, reverse=True):
            if source not in adjList:
                adjList[source] = []
            adjList[source].append(dest)

        result = []
        def dfs(source):
            while source in adjList and adjList[source]:
                dest = adjList[source].pop()
                dfs(dest)
            result.append(source)

        dfs("JFK")
        return result[::-1]
