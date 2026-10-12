class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {")" : "(", "}" : "{", "]" : "["}
        for c in s:
            if c in close:
                if not stack or stack.pop() != close.get(c):
                    return False
            else:
                stack.append(c)
        return not stack