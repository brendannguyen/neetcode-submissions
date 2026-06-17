class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        def getSquare(n):
            result = 0
            for c in str(n):
                result += int(c)**2
            return result
        
        while n not in seen:
            seen.add(n)
            n = getSquare(n)
            

            if n == 1:
                return True

        return False