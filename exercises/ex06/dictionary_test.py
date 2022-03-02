"""Testing for dictionary functions."""

__author__ = "730449161"


from dictionary import invert, favorite_color, count

import pytest


def test_invert_empty() -> None:
    """Tests an empty dictionary."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_invert_keyerror() -> None:
    """Test an key error dictionary."""
    with pytest.raises(KeyError):
        xs: dict[str, str] = {"on": "time", "in": "time"}
        invert(xs) 


def test_invert_words() -> None:
    """Tests a dictionary with words."""
    xs: dict[str, str] = {"UNC": "win", "Duke": "lose"}
    assert invert(xs) == {"win": "UNC", "lose": "Duke"}


def test_invert_letters() -> None:
    """Tests a dictionary with letters."""
    xs: dict[str, str] = {"a": "z", "b": "y", "c": "x"}
    assert invert(xs) == {"z": "a", "y": "b", "x": "c"}


def test_favorite_color_empty() -> None:
    """Tests a empty dictionary."""
    xs: dict[str, str] = dict()
    assert invert(xs) == {}


def test_favorite_color_many_items() -> None:
    """Tests a dictionary with many colors."""
    xs: dict[str, str] = {"Eden": "Green", "Nadia": "Lilac", "Krystal": "Black", "Chris": "Green"}
    assert favorite_color(xs) == "Green"


def test_favorite_color_one_item() -> None:
    """Tests a dictionary with one item."""
    xs: dict[str, str] = {"Chris": "Blue"}
    assert favorite_color(xs) == "Blue"


def test_count_empty() -> None:
    """Tests a list with one item."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_one_item() -> None:
    """Tests a list with one item."""
    xs: list[str] = ["happy"]
    assert count(xs) == {"happy": 1}


def test_count_many_items() -> None:
    """Tests a list with multiple items."""
    xs: list[str] = ["happy", "happy", "sad"]
    assert count(xs) == {"happy": 2, "sad": 1}