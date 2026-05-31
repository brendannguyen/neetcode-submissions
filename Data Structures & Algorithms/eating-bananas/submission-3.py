class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # brute force: for from 1 to max value in piles as k, to find minimum k speed, calc time taken (divide each pile by current k with rounding up)
        # use binary search to find k
        
        max_value = max(piles)
        min_speed = max_value
        
        low, high = 1, max_value

        while low < high:

            mid = low + (high-low) // 2

            time_count = 0
            for pile in piles:
                time_count += -(-pile // mid)

                if time_count > h:
                    break
            
            if time_count > h:
                low = mid+1
            else:
                min_speed = min(min_speed, mid)
                high = mid

                
        return min_speed