class Solution:
    def reverse(self, x: int) -> int:
        # % 10
        # to remain in 32-bit integer range:
        # check if last digit is greater than max 32-bit integer, if bigger, return 0
        # check if less than for negatives
        # check if all but last digit is bigger than max 32-bit integer digit but last one

        MIN = -2147483648  # -2^31,
        MAX = 2147483647  #  2^31 - 1

        result = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)

            if (result > MAX // 10) or (result == MAX // 10 and digit >= MAX % 10):
                return 0
            if (result < MIN // 10) or (result == MIN // 10 and digit <= MIN % 10):
                return 0
            
            result = (result * 10) + digit
        
        return result
