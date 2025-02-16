class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top_of_stack = -1
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
                top_of_stack = top_of_stack + 1
            elif i==')' and stack and stack[top_of_stack] == '(':
                stack.pop()
                top_of_stack = top_of_stack - 1
            elif i=='}' and len(stack)>0 and stack[top_of_stack] == '{':
                stack.pop()
                top_of_stack = top_of_stack - 1
            elif i==']' and len(stack)>0 and stack[top_of_stack] == '[':
                stack.pop()
                top_of_stack = top_of_stack - 1
            else:
                return False
        if not stack:
            return True
        else:
            return False
        