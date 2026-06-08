class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []

        def dfs(current_combo, open_count, closed_count):

            if len(current_combo) == (2*n):
                result.append("".join(current_combo))
                return

            # only explore open parenthesis path if under limit
            if open_count < n:
                current_combo.append('(')
                dfs(current_combo, open_count+1, closed_count)
                current_combo.pop()
            
            # only explore closed parenthesis path if less than open
            if closed_count < open_count:
                current_combo.append(')')
                dfs(current_combo, open_count, closed_count+1)
                current_combo.pop()

        dfs([], 0, 0)
        return result