from linknode.node import LinkNode
from linknode.reverse import reverse_v2


def get_public_seqs(head1, head2):
    """
    打印两个有序列表的公共序列，要求时间复杂度O(N)，额外空间复杂度O(1)
    :param head1:
    :param head2:
    :return:
    """
    public_parts = []
    while head1 and head2:
        if head1.value < head2.value:
            head1 = head1.next
            continue

        if head1.value == head2.value:
            public_parts.append(head1.value)
            head1 = head1.next
            head2 = head2.next
            continue

        if head1.value > head2.value:
            head2 = head2.next

    return public_parts


def find_middle(head):
    """
    通过快慢指针找到链表的中点
    :param head:
    :return:
    """
    if head is None:
        return

    fast = head
    slow = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def is_palindrome(head):
    if head is None:
        return False

    lp = head
    middle = find_middle(head)
    rev_head = reverse_v2(middle)
    lp.print()
    rev_head.print()

    rp = rev_head
    res = True
    while lp and rp:
        if lp.value != rp.value:
            res = False
            break

        lp = lp.next
        rp = rp.next

    # recovery head
    old_head = reverse_v2(rev_head)
    middle.next = old_head.next

    return res


def find_loop(head):
    """
    找到给定链表的入环节点

    解法1：使用列表记录沿途节点，每到新节点都检查节点是否已经存在，存在即为入环节点。
    解法2：快慢指针, 快指针一次走两步，慢指针一次走一步，当快慢指针相遇时，将快指针移到起点，然后快指针一次走一步，慢指针一次走一步，相遇点即为入环节点
    :param head:
    :return:
    """
    if head is None or head.next is None or head.next.next is None:
        return

    slow = head.next
    fast = head.next.next

    while slow != fast:
        if fast.next.next is None or slow.next is None:
            return None

        fast = fast.next.next
        slow = slow.next

    fast = head
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return fast


if __name__ == '__main__':
    n1 = LinkNode(1)
    n2 = LinkNode(2)
    n1.next = n2

    n3 = LinkNode(3)
    n2.next = n3

    n4 = LinkNode(4)
    n3.next = n4
    n4.next = n3
    print(find_loop(n1))
