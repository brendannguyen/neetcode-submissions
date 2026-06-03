# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # add two + any carry from previous, keep carry
        # if at end and have carry, create new node

        # how to deal with different lengths
        dummy = ListNode()
        cur_node = dummy
        l1_node = l1
        l2_node = l2
        carry = 0

        while l1_node or l2_node or carry:
            l1_value = l1_node.val if l1_node else 0
            l2_value = l2_node.val if l2_node else 0

            new_value = l1_value + l2_value + carry
            new_digit = new_value % 10
            carry = new_value // 10

            cur_node.next = ListNode(new_digit)

            cur_node = cur_node.next
            l1_node = None if not l1_node else l1_node.next
            l2_node = None if not l2_node else l2_node.next

        return dummy.next




