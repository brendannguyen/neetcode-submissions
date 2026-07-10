class Solution:
    def hammingWeight(self, n: int) -> int:
        # check if 1, then shift right by 1
        result = 0
        while n:
            if n & 1:
                result += 1
            n >>= 1

        return result