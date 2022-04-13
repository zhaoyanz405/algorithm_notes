class LinkNode:

    def __init__(self, value=0, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return str(self.value)

    def print(self):
        node = self
        vals = []
        while node:
            vals.append(node.value)
            node = node.next

        print('->'.join([str(v) for v in vals]))


def create_linknode(l):
    if not l:
        return None

    head = None
    cur = None

    for v in l:
        node = LinkNode(v)
        if head is None:
            cur = head = node
        else:
            cur.next = node
            cur = cur.next

    return head


if __name__ == '__main__':
    n = create_linknode([1, 2, 3, 4, 5])
    n.print()
