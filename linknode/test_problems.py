import pytest

from linknode.node import create_linknode
from linknode.problems import get_public_seqs, is_palindrome, find_middle


@pytest.mark.parametrize(
    'head1,head2,expected', [
        (create_linknode([1, 2, 3, 4, 5]), create_linknode([1, 3, 4, 6]), [1, 3, 4]),
        (None, create_linknode([1, 3, 4, 6]), []),
        (create_linknode([1, 2, 3, ]), create_linknode([4, 6]), []),
    ]
)
def test_get_public_seqs(head1, head2, expected):
    assert get_public_seqs(head1, head2) == expected


@pytest.mark.parametrize(
    'head,exp', [
        (create_linknode([]), False),
        (create_linknode([1]), True),
        (create_linknode([1, 2]), False),
        (create_linknode([1, 2, 1]), True),
    ]
)
def test_is_palindrome(head, exp):
    assert is_palindrome(head) == exp


@pytest.mark.parametrize(
    'head,exp', [
        (create_linknode([1]), 1),
        (create_linknode([1, 2]), 1),
        (create_linknode([1, 2, 3]), 2),
    ]
)
def test_find_middle(head, exp):
    assert find_middle(head).value == exp
