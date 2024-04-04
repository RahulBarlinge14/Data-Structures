class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        
        prev = head
        curr = head.next
        received_head = self.swapPairs(head.next.next)
        prev.next = received_head
        curr.next = prev
        return curr
