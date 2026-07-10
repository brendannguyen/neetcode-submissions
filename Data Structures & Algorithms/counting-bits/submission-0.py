class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n+1):
            cur = 0
            while i:
                if i & 1:
                    cur += 1
                i >>= 1
            result.append(cur)

        return result