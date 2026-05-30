class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                prev_i, prev_h = stack.pop()
                maxArea = max(maxArea, prev_h * (i - prev_i))
                start = prev_i

            stack.append((start, height))
        
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        
        return maxArea

        # add first bar to stack
        # for each bar afterwards
            # if the prev bar height is bigger, calculate prev bar area (compare) and pop (area can be found by height * current index - the prev bar index)
            # as the new bar can be expanded backwards, you take the prev index value
            # append the current bar height, and the prev index value (as it can be expanded backwards)

        
        # it is possible to be left with leftovers in the stack
        # all these leftover bars extend all the way to the end
        # so you iterate through each one, calc you area by height * (end of heights length - bar index) (compare)

        # return max area found
            