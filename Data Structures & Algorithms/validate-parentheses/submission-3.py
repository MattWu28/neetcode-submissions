class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_paren, close_paren = "({[", ")}]"
        for c in s:
            if c in open_paren:
                stack.append(c)
                continue
            if not stack:
                return False
            match c:
                case ")":
                    if stack.pop() != "(":
                        return False
                case "}":
                    if stack.pop() != "{":
                        return False
                case "]":
                    if stack.pop() != "[":
                        return False
        return not stack