from linknode.node import LinkNode


def reverse_v1(node: LinkNode):
    """
    压栈后反转
    :param node:
    :return:
    """
    # n1 -> n2 -> n3
    cur = node

    stack = []
    while cur:
        stack.append(cur.value)
        cur = cur.next

    head = None
    cur = None
    while stack:
        value = stack.pop()
        node = LinkNode(value)
        if head is None:
            cur = head = node
        else:
            cur.next = node
            cur = cur.next

    return head


def reverse_v2(node: LinkNode):
    """
    直接通过引用反转

    :param node:
    :return:
    """
    cur = node
    new_head = None
    while cur:
        cn = cur.next
        cur.next = new_head
        new_head = cur

        cur = cn

    return new_head


if __name__ == '__main__':
    n1 = LinkNode(1)
    n2 = LinkNode(2)
    n3 = LinkNode(3)

    n1.next = n2
    n2.next = n3

    n1.print()

    new_node = reverse_v2(n1)
    new_node.print()
