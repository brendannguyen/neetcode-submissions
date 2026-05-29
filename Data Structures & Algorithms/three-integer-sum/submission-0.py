class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) < 3:
            return []
        
        sorted_nums = sorted(nums)
        output = []
        # [-4, -1, -1, 0, 1, 2]

        # starting index is 0
        # l,r pointers
        # add left and right numbers to starting number
        # skip (+- 1) if that pointer hits starting index
        # if total is > 0, r-
        # if total is < 0, l+

        for i in range(len(sorted_nums)):
            l, r = 0, len(sorted_nums)-1

            while l < r:
                if l == i:
                    l += 1
                    continue
                if r == i:
                    r -= 1
                    continue

                cur = sorted_nums[l] + sorted_nums[i] + sorted_nums[r]

                if cur == 0:
                    new_triplet = sorted([sorted_nums[l], sorted_nums[i], sorted_nums[r]])
                    if new_triplet not in output:
                        output.append(new_triplet)
                
                if cur > 0:
                    r -= 1
                else:
                    l += 1

        return output