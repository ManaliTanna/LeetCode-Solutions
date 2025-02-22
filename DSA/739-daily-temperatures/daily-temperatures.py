class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #store results
        result = [0] * len(temperatures)
        stack = []
        # iterate throupgh temps
        for i, temp in enumerate(temperatures):

            # if bigger temp found
            while stack and temp > stack[-1][1]:
                # pop from stack
                j, t = stack.pop()

                # calculate difference and add to result
                result[j] = i - j

            # push the bigger value to stack
            stack.append([i, temp])
        return result