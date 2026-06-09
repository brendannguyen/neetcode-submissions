class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(word):
            l,r = 0, len(word)-1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1

            return True

        result = []
        current_result = []
        def dfs(i):
            
            if i >= len(s):
                result.append(current_result.copy())
                return
            
            for j in range(i, len(s)):
                if isPalindrome(s[i:j+1]):
                    current_result.append(s[i:j+1])
                    dfs(j+1)
                    current_result.pop()

        dfs(0)
        return result