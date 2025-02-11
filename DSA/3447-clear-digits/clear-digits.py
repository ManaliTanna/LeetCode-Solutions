class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isdigit(x):
            if x>0 and x<9:
                return True
        stack = []
        top_of_stack = 0
        for char in s:
            # print("char: ",char)
            if char.isdigit():
                # print("top: ",top_of_stack)
                top_of_stack = top_of_stack - 1
                stack.pop()
            else:
                top_of_stack = top_of_stack + 1
                # print("top: ",top_of_stack)
                stack.append(char)
        # print(stack)
        return "".join(stack)



        
        