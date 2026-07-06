class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # if == t: return 1
        # if len >= len(t) and != t: return 0
        # dfs
        # add
        # skip

        memo = {}

        def dfs(i, currentString):
            if currentString == t:
                return 1
            if (len(currentString) >= len(t) and currentString != t) or (i >= len(s)):
                return 0

            if (i, currentString) in memo:
                return memo[(i, currentString)]
            
            # add
            result = 0
            result += dfs(i+1, currentString + s[i])

            # skip
            result += dfs(i+1, currentString)

            memo[(i, currentString)] = result
            return result
        
        return dfs(0, "")