class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        l = len(part)

        for char in s:

            stack.append(char)

            # if complete match is found pop
            if "".join(stack[-l:]) == part:
                counter = l
                while counter > 0:
                    stack.pop()
                    counter = counter - 1

        return "".join(stack)


        