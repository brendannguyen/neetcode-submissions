class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)

        for i in range(n):
            l, r = i, i

            # odd
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

            # even
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1
        
        return result