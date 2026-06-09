class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # construct
        result = []
        mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        current_result = []
        def dfs(i):

            if current_result and len(current_result) == len(digits):
                result.append("".join(current_result))
                return

            if i >= len(digits):
                return


            
            digit = digits[i]
            characters = mapping[digit]
            
            for j in range(len(characters)):
                current_result.append(characters[j])
                print(current_result)
                dfs(i+1)
                current_result.pop()

        dfs(0)
        return result