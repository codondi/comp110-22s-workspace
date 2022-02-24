"""Testing for utils functions."""

__author__ = "730449161"


from utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests empty set."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_single_item() -> None:
    """Tests set of one item."""
    xs: list[int] = [2]
    assert only_evens(xs) == [2]


def test_only_evens_many_items_() -> None:
    """Tests set of many items."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert only_evens(xs) == [2, 4, 6, 8, 10]


def test_sub_empyt() -> None:
    """Tests empty set."""
    xs: list[int] = []
    assert sub(xs, 3, 5) == []


def test_sub_short_list() -> None:
    """Tests short set."""
    xs: list[int] = [1, 2]
    assert sub(xs, 0, 1) == [1]


def test_sub_long_list() -> None:
    """Tests long set."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sub(xs, 3, 5) == [4, 5]


def test_concat_empty() -> None:
    """Tests empty set."""
    xs: list[int] = []
    xy: list[int] = []
    assert concat(xs, xy) == []


def test_concat_lists_with_diffferent_numbers() -> None:
    """Tests lists with different numbers."""
    xs: list[int] = [1, 2, 3, 4, 5]
    xy: list[int] = [6, 7, 8, 9, 10]
    assert concat(xs, xy) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_concat_with_same_numbers() -> None:
    """Tests lists with the same numbers."""
    xs: list[int] = [1, 2, 3]
    xy: list[int] = [1, 2, 3]
    assert concat(xs, xy) == [1, 2, 3, 1, 2, 3]
