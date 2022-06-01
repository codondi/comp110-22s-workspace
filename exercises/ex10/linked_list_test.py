"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, is_equal, max, linkify, scale

__author__ = "730449161"


def test_is_equal_non_empty_equal() -> None:
    """When comparing two equal nodes."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(linked_list, Node(1, Node(2, Node(3, None)))) is True


def test_is_equal_one_empty_not_equal() -> None:
    """When comparing two uneqal nodes, where one is empty."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(linked_list, None) is False


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_non_empty() -> None:
    """Value_at of a non-empty node should return value at specified index."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_value_at_empty() -> None:
    """Value_at of a empty node should raise an error."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_max_non_empty() -> None:
    """Max of a non-empty node should return specified value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_empty() -> None:
    """Max of an empty node should raise ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify_non_empty() -> None:
    """Linkify should turn non empty list into nodes."""
    xs: list[int] = [1, 2, 3]
    assert is_equal(linkify(xs), Node(1, Node(2, Node(3, None))))


def test_linkify_empty() -> None:
    """Linkify should take empty list and return None."""
    xs: list[int] = []
    assert linkify(xs) is None


def test_scale_non_empty() -> None:
    """Scale should take non-empty node and multiply data attribute by the given factor."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert is_equal(scale(linked_list, 3), Node(3, Node(6, Node(9, None))))


def test_scale_empty() -> None:
    """Scale should take empty node and return value error."""
    assert scale(None, 3) is None