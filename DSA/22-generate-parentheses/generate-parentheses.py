class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []

        def backtrack(no_of_open, no_of_close):

            # base case all n brackets used up correctly
            if no_of_open == no_of_close == n:
                ans = "".join(stack)
                result.append(ans)
                return

            #push ( to stack only if open < n
            if no_of_open < n:
                stack.append('(')
                # print("Added (")
                backtrack(no_of_open + 1, no_of_close)
                stack.pop()

            if no_of_open > no_of_close and no_of_close < n:
                stack.append(')')
                # print("Added )")
                backtrack(no_of_open, no_of_close + 1)
                stack.pop()
        
        backtrack(0,0)
        return result


        