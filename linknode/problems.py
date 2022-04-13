import pytest

from linknode.node import create_linknode


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


@pytest.mark.parametrize(
    'head1,head2,expected', [
        (create_linknode([1, 2, 3, 4, 5]), create_linknode([1, 3, 4, 6]), [1, 3, 4]),
        (None, create_linknode([1, 3, 4, 6]), []),
        (create_linknode([1, 2, 3, ]), create_linknode([4, 6]), []),
    ]
)
def test_get_public_seqs(head1, head2, expected):
    assert get_public_seqs(head1, head2) == expected
