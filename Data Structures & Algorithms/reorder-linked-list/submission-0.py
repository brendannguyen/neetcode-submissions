# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
    
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev_node = None
        cur_node = slow.next
        slow.next = None

        while cur_node:
            cur_next = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = cur_next
        
        left_node = head
        right_node = prev_node

        while right_node:
            left_next = left_node.next
            right_next = right_node.next

            left_node.next = right_node
            right_node.next = left_next

            left_node = left_next
            right_node = right_next
        
        