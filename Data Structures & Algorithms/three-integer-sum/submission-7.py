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
            
            if sorted_nums[i] > 0:
                break

            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            l, r = i + 1, len(sorted_nums)-1

            while l < r:
                cur = sorted_nums[l] + sorted_nums[i] + sorted_nums[r]

                if cur > 0:
                    r -= 1
                elif cur < 0:
                    l += 1
                else:
                    output.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    r -= 1
                    while sorted_nums[l] == sorted_nums[l-1] and l < r:
                        l += 1

        return output