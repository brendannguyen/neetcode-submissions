# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            return False

        left_node = head
        right_node = head.next

        while left_node and right_node:

            left_node = left_node.next
            right_node = right_node.next

            if not right_node:
                return False
            right_node = right_node.next

            if left_node == right_node:
                return True
            

        
        return False