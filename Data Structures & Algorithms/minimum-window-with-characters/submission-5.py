class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        seen = {}
        l,r = 0,len(t)-1
        minString = s + t

        for i in range(len(t)):
            seen[t[i]] = seen.get(t[i], 0) - 1
            seen[s[i]] = seen.get(s[i], 0) + 1

        while r < len(s) and l < len(s):

            if r >= len(t):
                seen[s[r]] = seen.get(s[r], 0) + 1

            while min(seen.values()) >= 0:
                
                if (r-l+1) < len(minString):
                    minString = s[l:r+1]
                print(s[l:r+1])

                seen[s[l]] = seen.get(s[l], 0) - 1
                l += 1
            else:
                r += 1

        return minString if len(minString) <= len(s) else ""