class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # XOR
        # exactly one of two can be true
        # a ^ a = 0, a ^ 0 = a, a ^ a = not a (inverse)

        result = 0
        for num in nums:
            result = result ^ num
        
        return result