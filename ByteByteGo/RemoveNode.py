from ds import ListNode

def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy  

    for _ in range(k):
        if fast.next is None:
            return head
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next  

    return dummy.next
