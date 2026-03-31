class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for score in operations:
            if score == "+":
                stack.append(stack[-2] + stack[-1])
            elif score == "D":
                stack.append(stack[-1] * 2)
            elif score == "C":
                stack.pop(-1)
            else:
                stack.append(int(score))
        return sum(stack)
