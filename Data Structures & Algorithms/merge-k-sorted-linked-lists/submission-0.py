# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # minheap (smallest val on top log(k))

        minHeap = []
        dummy = ListNode()
        counter = 0

        for l in lists:
            if l:
                heapq.heappush(minHeap, (l.val, counter, l))
                counter += 1

        
        cur = dummy
        while minHeap:
            cur.next = heapq.heappop(minHeap)[2]
            cur = cur.next

            if cur.next:
                heapq.heappush(minHeap, (cur.next.val, counter, cur.next))
                counter += 1


        return dummy.next



