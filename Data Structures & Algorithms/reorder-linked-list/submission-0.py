# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        p1 = head
        p2 = self.reverse(slow.next)
        slow.next = None

        while p2:
            temp1, temp2 = p1.next, p2.next
            p1.next = p2
            p2.next = temp1
            p1, p2 = temp1, temp2


    
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
