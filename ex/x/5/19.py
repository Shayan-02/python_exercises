# https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_map = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in parentheses_map.values():
                stack.append(c)
            elif c in parentheses_map:
                if not stack or stack.pop() != parentheses_map[c]:
                    return False
        return not stack

        