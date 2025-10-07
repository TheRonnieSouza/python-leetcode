#https://leetcode.com/problems/valid-parentheses/description/

class SolutionValidParentheses:
    
    def is_valid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        return len(stack) == 0 