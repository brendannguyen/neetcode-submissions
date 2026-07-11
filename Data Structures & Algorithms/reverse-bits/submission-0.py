class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # get ith bit of n
            bit = (n >> i) & 1
            # shift bit to positon (31-i) and add to result
            result += (bit << (31-i))
        return result