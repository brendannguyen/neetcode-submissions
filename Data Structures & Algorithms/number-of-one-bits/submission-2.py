class Solution:
    def hammingWeight(self, n: int) -> int:
        # subtracting 1 from number -> rightmost 1 flips to 0, and all right bits after turn to 1
        # performing (n & (n-1)) removes rightmost 1 bit from n

        result = 0
        while n:
            n = n & (n-1)
            result += 1
        
        return result