from ds import ListNode

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def linked_list_reversal(head: ListNode) -> ListNode:
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
