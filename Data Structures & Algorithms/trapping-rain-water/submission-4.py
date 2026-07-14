class Solution:
    def trap(self, height: List[int]) -> int:
        totalArea = 0
        l, r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax > rightMax:
                r -= 1
                rightMax = max(rightMax, height[r])
                totalArea += rightMax - height[r]
            else:
                l += 1
                leftMax = max(leftMax, height[l])
                totalArea += leftMax - height[l]

        return totalArea