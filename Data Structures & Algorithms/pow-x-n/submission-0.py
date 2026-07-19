class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            result = pow(x*x, n//2)
            return result*x if n%2 else result

        result = pow(x, abs(n))
        return result if n >= 0 else 1/result