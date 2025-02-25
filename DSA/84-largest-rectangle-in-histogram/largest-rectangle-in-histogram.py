class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for curr_idx, curr_height in enumerate(heights):
            start = curr_idx
            while stack and curr_height < stack[-1][1]:

                # If smaller rectangle comes, we pop the bigger one (top of stack)
                i, h = stack.pop()

                # Calculate area of the popped rectangle
                maxArea = max(maxArea, h * (curr_idx-i) )

                # The new height can extend backwards
                start = i
    
            # append index and new height
            stack.append((start,curr_height))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i) )

        return maxArea
