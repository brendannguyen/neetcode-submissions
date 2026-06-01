class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        l, r = 0, 0
        seen = {}
        for s in s1:
            seen[s] = seen.get(s, 0) - 1

        while r < len(s2):
            seen[s2[r]] = seen.get(s2[r], 0) + 1
            print(min(seen.values()))
            if min(seen.values()) < 0:
                if (r-l+1) >= len(s1):
                    seen[s2[l]] = seen.get(s2[l], 0) - 1
                    l += 1
                r += 1
            else:
                return True
            

        return False
        # space O(26)
