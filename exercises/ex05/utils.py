"""List utility functions."""

__author__ = "730449161"


def only_evens(input_list: list[int]) -> list[int]:
    """Returns a list of evens from the string."""
    evens_list: list[int] = []
    for element in input_list:
        if element % 2 == 0:
            evens_list.append(element)
    return evens_list


def sub(input_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a subset of the inputed list, between distinct indices."""
    i: int = start_index
    subset_list: list[int] = []
    if start_index < 0:
        start_index = 0
        i = 0
    if input_list == [] or start_index >= len(input_list) or end_index <= 0:
        return []
    if end_index > len(input_list):
        end_index = len(input_list)
    while i >= start_index and i < end_index:
        subset_list.append(input_list[i])
        i += 1
    return subset_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Takes a list and adds a second list to the first."""
    total_list: list[int] = list_one + list_two
    return total_list