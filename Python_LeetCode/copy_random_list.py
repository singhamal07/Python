class Node:
    def __init__(self, x: int, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        old_to_new = {}  # original node -> copied node

        # Pass 1: create all new nodes
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: assign next and random pointers
        curr = head
        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]

# Helper to build a linked list from a list of [val, random_index] pairs
def build_list(data):
    if not data:
        return None
    nodes = [Node(val) for val, _ in data]
    for i, (_, rand_idx) in enumerate(data):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return nodes[0]

# Helper to convert linked list to list of [val, random_index] for verification
def list_to_output(head):
    nodes, result = [], []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    node_index = {node: i for i, node in enumerate(nodes)}
    for node in nodes:
        rand_idx = node_index[node.random] if node.random else None
        result.append([node.val, rand_idx])
    return result