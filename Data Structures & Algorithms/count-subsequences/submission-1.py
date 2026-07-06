class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        # if == t: return 1
        # if len >= len(t) and != t: return 0
        # dfs
        # add
        # skip

        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i >= len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            # skip
            result = dfs(i+1, j)

            # add if match
            if s[i] == t[j]:
                result += dfs(i+1, j+1)

            memo[(i, j)] = result
            return result
        
        return dfs(0, 0)