class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        memo = {}

        def dfs(i, j):
            if i == m:
                # end of word1, must insert all remaining word2 chars
                return n-j
            if j == n:
                # end of word2, must delete all remaining word1 chars
                return m-i
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            result = 0
            if word1[i] == word2[j]:
                result += dfs(i+1, j+1)
            else:
                result += min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1))+1
            
            memo[(i, j)] = result
            return memo[(i, j)]

        return dfs(0, 0)
