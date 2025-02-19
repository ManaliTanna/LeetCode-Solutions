class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def operate(var1, var2, operator):
            if operator == '+':
                # print("Adding ", var1, var2)
                return var1+var2
                
            elif operator == '*':
                # print("Multiplying ", var1, var2)
                return var1*var2
                
            elif operator == '-':
                # print("Subtracting ", var1, var2)
                return var2-var1
                
            elif operator == '/':
                # print("Dividing ", var2, var1)
                return var2/var1
            else:
                return "Default case"

        stack = []
        for i in tokens:
            if i in ["+","-","*","/"]:
                if stack:
                    var1 = int(stack.pop())
                    var2 = int(stack.pop())
                    ans = operate(var1, var2, i)
                    stack.append(ans)
                    # print(stack)
            else:
                stack.append(i)

        return int(stack[0])
        