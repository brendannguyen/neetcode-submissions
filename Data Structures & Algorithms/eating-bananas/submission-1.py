class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:



        # every hour
        # can eat from one pile of bananas at k rate
        # find minimum k rate to eat all bananas within h hours
        # 

        # largest first?

        # N * log(M)

        # for each pile, between max bananas and 1, binary search for minimum speed for each pile?

        # brute force
        
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