class Solution:
    def isValid(self, s: str) -> bool:
        left_open = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char in left_open:
                if stack and stack[-1] == left_open[char]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)              
        return stack == []

