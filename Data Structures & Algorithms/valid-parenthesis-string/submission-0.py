class Solution:
    def checkValidString(self, s: str) -> bool:
        openStack, wildcardStack = [], []
        for i, char in enumerate(s):
            if char == '(':
                openStack.append(i)
            elif char == '*':
                wildcardStack.append(i)
            else:
                if not openStack and not wildcardStack:
                    return False
                if openStack:
                    openStack.pop()
                else:
                    wildcardStack.pop()
        
        while openStack and wildcardStack:
            if openStack.pop() > wildcardStack.pop():
                return False

        return len(openStack) == 0