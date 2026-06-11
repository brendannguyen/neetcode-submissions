# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # O(n)
        n = 0
        cur = head
        while cur:
            cur = cur.next
            n += 1

        # O(n)
        def reverse(head, k, n):
            if not head :
                return None
            
            count = 0
            prev_node, cur_node = None, head
            end_node = None

            while count < k and cur_node:
                
                cur_next = cur_node.next
                cur_node.next = prev_node
                prev_node = cur_node
                cur_node = cur_next

                count += 1
                if count == k:
                    end_node = cur_next

            if n-k >= k:
                head.next = reverse(end_node, k, n-k)
            else:
                head.next = end_node
            return prev_node

        return reverse(head, k, n)

