class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # X -> 1
        # Y ->  (X: 1, Y: 1)
        # Y ->  (X: 1, Y: 2)
        # X -> (X: 2, Y: 2)


        # A -> (A: 1)
        # A -> (A: 2)
        # A -> (A: 3)
        # B -> (A: 3, B: 1)
        # A -> (A: 4, B: 1)
        # B -> (A: 4, B: 2) - end 

        # total - highest count
        # end when smallest char count > k
        # l += 1 until smallest char count <= k
        # every iteration of right pointer, check max? (length = r-l+1)


        counts = {}
        result = 0
        l = 0
        highestCount = 0

        for r in range(len(s)):
            if s[r] in counts:
                counts[s[r]] += 1
            else:
                counts[s[r]] = 1
            
            highestCount = max(highestCount, counts[s[r]])

            while (r-l+1) - highestCount > k:
                counts[s[l]] -= 1
                l += 1


            result = max(result, r-l+1)


        return result 
            




