# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        left_node = right_node = head

        while right_node and right_node.next:

            left_node = left_node.next
            right_node = right_node.next.next

            if left_node == right_node:
                return True

        return False