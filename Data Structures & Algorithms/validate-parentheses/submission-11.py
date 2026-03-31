class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if stack and stack[-1] == hashmap[char]:
                    stack.pop(-1)
                else:
                    return False

        return stack == []
