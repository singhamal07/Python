from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd = head
        even = head.next
        even_head = even  # save start of even list to attach later

        while even and even.next:
            odd.next = even.next   # link odd to next odd
            odd = odd.next         # advance odd pointer
            even.next = odd.next   # link even to next even
            even = even.next       # advance even pointer

        odd.next = even_head       # attach even list after odd list
        return head
