class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        

        # without sorting

        # value -> number of connections
        # 2: 0
        # 20: 0
        # 4: 0
        #10: 0
        # 3: 2
        # 4: 3
        # 5: 4

        max_seq = 0
        count = {}

        for num in nums:
            if not count.get(num, 0):
                count[num] = count.get(num-1, 0) + count.get(num+1, 0) + 1

                count[num - count.get(num-1, 0)] = count[num]
                count[num + count.get(num+1, 0)] = count[num]

                max_seq = max(max_seq, count[num])

        return max_seq