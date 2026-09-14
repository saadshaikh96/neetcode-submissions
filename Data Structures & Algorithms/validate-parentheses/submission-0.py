class Solution:
    def isValid(self, s: str) -> bool:
        map = {']':'[', '}':'{', ')':'('}
        stack = []
        for bracket in s:
            if bracket not in map:
                stack.append(bracket)
            else:
                if not stack or stack[-1] != map[bracket]:
                    return False
                stack.pop()
                
        return len(stack) == 0