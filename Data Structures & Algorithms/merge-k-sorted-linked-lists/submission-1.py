# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        queue = []
        
        for l in lists:
            cur = l
            while cur:
                queue.append(cur)
                cur = cur.next
        
        if not queue:
            return None
        
        dummy.next = queue.pop()
        
        while queue:
            cur = dummy.next
            prev = dummy
            node = queue.pop()

            while cur:
                if cur.val >= node.val:
                    break
                prev = cur
                cur = cur.next
                

            prev.next = node
            node.next = cur
    
        return dummy.next

        
        