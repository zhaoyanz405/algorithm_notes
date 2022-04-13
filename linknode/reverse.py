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

    final_node = None
    cur = None
    while stack:
        value = stack.pop()
        node = LinkNode(value)
        if cur is None:
            cur = final_node = node
        else:
            cur.next = node
            cur = cur.next

    return final_node


if __name__ == '__main__':
    n1 = LinkNode(1)
    n2 = LinkNode(2)
    n3 = LinkNode(3)

    n1.next = n2
    n2.next = n3

    reverse_v1(n1)
    print(n1.next)
    print(n2.next)
    print(n3.next)
