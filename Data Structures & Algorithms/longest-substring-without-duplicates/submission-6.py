class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,0
        seen = {}
        maxLength = 0

        while r < len(s):
            if s[r] in seen:
                l = max(l, seen[s[r]] + 1)

            seen[s[r]] = r
            maxLength = max(maxLength, r-l+1)
            r += 1 

        return maxLength
