class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # count hand cards
        count = {}
        for c in hand:
            count[c] = count.get(c, 0) + 1

        minHeap = list(count.keys())
        heapq.heapify(minHeap)
        while minHeap:
            current = minHeap[0]
            for i in range(current, current + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True
