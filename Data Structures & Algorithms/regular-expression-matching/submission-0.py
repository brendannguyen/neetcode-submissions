class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # i, j
        # if s[i] == p[j] or p[j] == 'x': i+1, j+1
        # if s[i] != p[j]:
            # if p[j] == '*': 
                # skip
                # match one or more
                # i+

        # if i >= len(s): return True
        # if j >= len(p): return True

        memo = {}

        def dfs(i, j):
            if j >= len(p):
                return i >= len(s)
            
            if (i, j) in memo:
                return memo[(i, j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if (j+1) < len(p) and p[j+1] == '*':
                memo[(i, j)] = dfs(i, j+2) or (match and dfs(i+1, j))
                return memo[(i, j)]
            
            if match:
                memo[(i, j)] = dfs(i+1, j+1)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False


        return dfs(0, 0)