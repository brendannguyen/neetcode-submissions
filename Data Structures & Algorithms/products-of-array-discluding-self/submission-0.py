class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # naive:
        # loop every time 

        # better:
        # product / current num
        # count zeros first
        sums = []

        product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        if zero_count > 1:
            return [0]*len(nums)

        for i in range(len(nums)):
            if zero_count != 0:
                if nums[i] != 0:
                    sums.append(0)
                else:
                    sums.append(product)
            else:
                sums.append(product // nums[i])

        return sums