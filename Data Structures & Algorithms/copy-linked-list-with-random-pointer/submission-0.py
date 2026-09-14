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
        from collections import defaultdict
        map = defaultdict(lambda: Node(0))
        map[None] = None

        ptr = head
        while ptr:
            map[ptr].val = ptr.val
            map[ptr].next = map[ptr.next]
            map[ptr].random = map[ptr.random]
            ptr = ptr.next

        return map[head]
        