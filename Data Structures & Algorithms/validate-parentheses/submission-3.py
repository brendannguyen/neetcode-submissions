class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 1:
            return False
        
        stack = []
        

        for c in s:
            if c == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
                else:
                    continue
            
            if c == ')':
                if len(stack) == 0 or stack.pop() != '(':
                    return False
                else:
                    continue
            
            if c == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
                else:
                    continue

            stack.append(c)
        
        return len(stack) == 0