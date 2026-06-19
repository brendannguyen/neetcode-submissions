class Solution:
    def longestPalindrome(self, s: str) -> str:
        resultIdx, resultLen = 0, 0
        n = len(s)

        # O(n^2)
        # palindrome: first and last chars are the same, and inner characters are a palindrome
        # palindrome: substring is <= 2, and first and last chars are same, must be palindrome

        dp = [[False] * n for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                # if first and last chars equal
                # and if current substring is <= 2 in length or we already know this inner substring is true
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resultLen < (j-i+1):
                        resultLen = j-i+1
                        resultIdx = i
        
        return s[resultIdx:resultIdx + resultLen]