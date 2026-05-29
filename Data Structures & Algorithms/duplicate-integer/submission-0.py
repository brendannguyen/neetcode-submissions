class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # set() add to set, if already in set, return truee
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)


        return False