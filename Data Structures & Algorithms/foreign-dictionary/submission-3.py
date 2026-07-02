class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adjList = {c: set() for w in words for c in w}

        for i in range(n-1):
            for j in range(len(words[i])):
                if j > len(words[i+1])-1:
                    
                    if words[i][:j] == words[i+1][:j]:
                        return ""
                    break
    
                if words[i][j] != words[i+1][j]:
                    adjList[words[i][j]].add(words[i+1][j])
                    break
        

        visited = {}
        result = []

        def dfs(c):
            if c in visited:
                return visited[c] # True

            visited[c] = True
            for nei in adjList[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            result.append(c)

        for c in adjList.keys():
            if dfs(c):
                return "" # theres a cycle
        
        return "".join(result[::-1])

