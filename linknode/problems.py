from linknode.node import create_linknode
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


if __name__ == '__main__':
    head = create_linknode([1, 2, 3, 2, 1])
    assert is_palindrome(head)