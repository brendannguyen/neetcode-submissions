class Solution:
    def checkValidString(self, s: str) -> bool:
        
        pStack = []
        aStack = []

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                pStack.append(i)
            elif c == '*':
                aStack.append(i)
            else:
                if (not pStack and not aStack):
                    return False
                
                # if pstack.pop != ), try aStack else return False
                if pStack:
                    pStack.pop()
                else:
                    aStack.pop()

        while pStack and aStack:
            # '(' goes after corresponding '*'
            if pStack.pop() > aStack.pop():
                return False
        
        return len(pStack) == 0