"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # weave copies with originals
        cur_node = head
        while cur_node:
            copy = Node(cur_node.val)
            copy.next = cur_node.next
            cur_node.next = copy
            cur_node = copy.next
        
        #  assign random pointers
        cur_node = head
        while cur_node:
            if cur_node.random:
                cur_node.next.random = cur_node.random.next
            cur_node = cur_node.next.next

        # unweave
        cur_node = head
        copy_head = head.next

        while cur_node:
            copy = cur_node.next
            cur_node.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            
            cur_node = cur_node.next

        return copy_head




