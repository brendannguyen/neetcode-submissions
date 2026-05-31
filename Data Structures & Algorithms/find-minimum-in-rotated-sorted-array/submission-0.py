class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        # problem: how to find min value?
        # binary search for n? (the rotation as rotation must be between 1 and n)
        # after finding n, you can just do nums[n], if n == len(n), set n to 0

        # but how to know that the current n rotation is correct?
        # if nums[n-1] is > than nums[n], then must be start


        low, high = 0, len(nums)
        min_val = nums[0]

        while low < high:

            mid = low + (high-low) // 2
            print(f'{mid}: {nums[mid]}')
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

        # 7 > 5, go smaller

        # 1
        # [4,5,6,7]
        # nums[-1] > nums[0]
