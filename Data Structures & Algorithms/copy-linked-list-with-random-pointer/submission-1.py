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
        
        copied = {}
        cur_node = head

        while cur_node:
            copied[cur_node] = Node(cur_node.val, cur_node.next, cur_node.random)
            cur_node = cur_node.next
        
        cur_node = head
        while cur_node:
            temp = cur_node.next
            copied[cur_node].next = None if not temp else copied[temp]
            copied[cur_node].random = None if not cur_node.random else copied[cur_node.random]
            cur_node = cur_node.next

        return copied[head]
