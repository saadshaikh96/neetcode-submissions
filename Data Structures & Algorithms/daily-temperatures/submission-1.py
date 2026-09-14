class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for temp in temperatures]
        stack = [len(temperatures) - 1]
        
        for i in reversed(range(len(temperatures) - 1)):
            currentTemperature = temperatures[i]
            while stack and currentTemperature >= temperatures[stack[-1]]:
                stack.pop()
            result[i] = 0 if not stack else stack[-1] - i
            stack.append(i)

        return result