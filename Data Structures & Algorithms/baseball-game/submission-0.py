class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        i = 0
        for score in operations:
            if score == "+":
                stack.append(stack[-2] + stack[-1])
                i += 1
            elif score == "D":
                stack.append(stack[-1] * 2)
                i += 1
            elif score == "C":
                stack.pop(-1)
                i -= 1
            else:
                stack.append(int(score))
        return sum(stack)
