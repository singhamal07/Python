from ds import ListNode

def linked_list_intersection(head_A: ListNode, head_B: ListNode) -> ListNode:
    if not head_A or not head_B:
        return None

    p1, p2 = head_A, head_B

    while p1 != p2:
        p1 = p1.next if p1 else head_B
        p2 = p2.next if p2 else head_A
    return p1
