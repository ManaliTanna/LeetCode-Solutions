class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # pointers to track the area formed 
        l_ptr = 0
        r_ptr = len(height) - 1

        # store max area
        max_area = 0

        # iterate while pointers dont cross each other or exceed array
        while l_ptr<r_ptr and l_ptr<len(height) and r_ptr>0:

            print(l_ptr,height[l_ptr],r_ptr,height[r_ptr])

            # find the smaller height
            smaller_height = min(height[l_ptr],height[r_ptr])

            print(smaller_height)

            print(smaller_height*abs(r_ptr - l_ptr))

            max_area = max(max_area, smaller_height*abs(r_ptr - l_ptr))

            if smaller_height == height[l_ptr]:
                l_ptr = l_ptr + 1
            else:
                r_ptr = r_ptr - 1

        return max_area

        # # brute force

        # # store max area formed
        # max_area = 0

        # # store area in each iteration
        # area = 0

        # # iterate through lines
        # for i in range(0,len(height)):
        #     for j in range(i+1,len(height)):

        #         # area cannot overflow so we need to select the smaller line of the two
        #         smaller_height = min(height[i],height[j])

        #         # calculate area but multiple difference between index and smalled line height
        #         area = smaller_height * (j-i)

        #         # update max
        #         max_area = max(max_area,area)
        
        # return max_area
        