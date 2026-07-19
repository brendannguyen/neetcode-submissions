class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = 1
        power = abs(n)

        while power:
            # if odd, multply by extra x
            if power & 1:
                result *= x
            
            # square base
            x *= x
            # divide exponent by 2
            power >>= 1
        
        return result if n>=0 else 1/result