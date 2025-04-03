from ds import MultiLevelListNode

def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    if not head:
        return None
    
    tail = head

    while tail.next:
        tail = tail.next
    
    curr = head

    while curr:
        if curr.child:

            tail.next = curr.child

            curr.child = None

            while tail.next:
                tail = tail.next
        curr = curr.next
    
    return head
