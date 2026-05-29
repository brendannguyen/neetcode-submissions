class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap
        # count occurrences, and then se min heap
        # remove values with occurences that are > k

        # O(n)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        heap = []
        for num in counts.keys():
            heapq.heappush(heap, (counts[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output