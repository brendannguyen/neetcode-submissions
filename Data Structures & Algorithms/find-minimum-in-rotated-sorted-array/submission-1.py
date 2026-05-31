class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # problem: how to find min value?
        # binary search for n? (the rotation as rotation must be between 1 and n)

        # but how to know that the current n rotation is correct?
        # if nums[n-1] is > than nums[n], then must be start


        low, high = 0, len(nums)
        min_val = nums[0]

        while low < high:
            mid = low + (high-low) // 2

            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] > min_val:
                low = mid+1
            else:
                high=mid

        return min_val

        
        # [5,6,7,4]

        # 2

        # [7,4,5,6]

        # 7 > 5, rotate more to right (if less than, rotate less to right)
        
        # 1
        # [4,5,6,7]
        # nums[-1] > nums[0]
