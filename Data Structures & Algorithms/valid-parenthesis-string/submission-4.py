class Solution:
    def checkValidString(self, s: str) -> bool:
        # greedy
        pMin = 0
        pMax = 0

        for c in s:
            if c == '(':
                pMin += 1
                pMax += 1
            elif c == ')':
                pMin -= 1
                pMax -= 1
            else:
                pMin -= 1
                pMax += 1
            
            if pMax < 0:
                return False # too many ')'
            if pMin < 0:
                pMin = 0
            
        return pMin == 0