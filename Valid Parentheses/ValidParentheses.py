class Solution(object):
    def isValid(self, s):
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char in pairs:
                if not stack:
                    return False
                if stack[-1] != pairs[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0