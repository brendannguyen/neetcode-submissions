class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = len(temperatures)*[0]

        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                result[index] = i - index

            stack.append((temperatures[i], i))

            
        return result  