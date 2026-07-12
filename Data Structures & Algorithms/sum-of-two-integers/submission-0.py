class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        result = 0
        mask = 0xFFFFFFFF

        for i in range(32):
            aBit = (a >> i) & 1
            bBit = (b >> i) & 1

            # XOR
            curr = aBit ^ bBit ^ carry
            carry = (aBit + bBit + carry) >= 2
            # set ith bit if curr is 1
            if curr:
                result |= (1 << i)

        # if result is negative, convert to signed integer
        if result > 0x7FFFFFFF:
            result = ~(result ^ mask)
        
        return result