class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens:
            if c == '+':
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif c == '-':
                a, b = stack.pop(), stack.pop()
                result = b - a
                stack.append(result)
            elif c == '*':
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif c == '/':
                a, b = stack.pop(), stack.pop()
                result = int(b / a)
                stack.append(result)
            else:
                stack.append(int(c))

        return stack.pop()