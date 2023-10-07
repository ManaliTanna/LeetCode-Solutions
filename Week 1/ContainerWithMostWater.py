class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_ptr = 0
        right_ptr = len(height)-1
        max_area = 0
        while (left_ptr < right_ptr):
            if(height[left_ptr] < height[right_ptr]):
                area = height[left_ptr] * (right_ptr - left_ptr)
                left_ptr = left_ptr + 1
            else:
                area = height[right_ptr] * (right_ptr - left_ptr)
                right_ptr = right_ptr - 1
            max_area = max(area, max_area)
        return max_area
    
        """
        Brute force - time limit exceeded
        left_ptr = 0
        right_ptr = len(height)-1
        max_area = 0
        for left_ptr in range(0,len(height)):
            for right_ptr in range (left_ptr + 1, len(height)):
                if(height[left_ptr] < height[right_ptr]):
                    area = height[left_ptr] * (right_ptr-left_ptr)
                else:
                    area = height[right_ptr] * (right_ptr-left_ptr)
                if area > max_area:
                    max_area = area
        return max_area
        """