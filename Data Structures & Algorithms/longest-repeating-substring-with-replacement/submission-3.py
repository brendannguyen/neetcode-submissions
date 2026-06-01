class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l,r = 0,0
        seen = {}
        maxLength = 0
        maxFreq = 0 # O(n) instead of (O(26*n) = O(n))

        while r < len(s):
            seen[s[r]] = seen.get(s[r], 0) + 1

            maxFreq = max(maxFreq, seen[s[r]])

            if (r - l + 1) - maxFreq <= k:
                maxLength = max(maxLength, (r-l+1))

            while (r - l + 1) - maxFreq > k:
                    seen[s[l]] = seen[s[l]] - 1
                    l += 1
            
            r += 1

        return maxLength


        #0,0 - A: 1 -> 1-1 <= 1, maxLength = 1
        #0,1 - A: 2 -> 2-2 <= 1, maxLength = 2
        #0,2 - A: 3 -> 3-3 <= 1, maxLength = 3
        #0,3 - A: 3, B:1 -> 4-3 <= 1, maxLength = 4
        #0,4 - A: 4, B: 1 -> 5-4 <= 1, maxLength = 5
        #0,5 - A:4, B: 2 -> 6-4 <= 1 (no), maxLength = 5
        #1,5 - A: 3, B: 2 -> 5-3 <= 2 (no)
        #2,5 - A: 2, B:2 -> 4-2 <= 2 (no)
        #3,5 - A: 1, B:2 -> 3-1 <= 2 (no)