class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        found = set()
        for n in nums:
            found.add(n)
        
        for i in range(len(nums)+1):
            if i not in found:
                return i