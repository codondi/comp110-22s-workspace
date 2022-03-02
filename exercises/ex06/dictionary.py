"""Creating dictionary functions."""

__author__ = "730449161"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Inverts the key and values stored in a dictionary."""
    inverted: dict[str, str] = dict()
    for key in original:
        if original[key] in inverted:
            raise KeyError("Cannont invert a string that will result in multiple key values.")
        inverted[original[key]] = key
    return inverted


def favorite_color(info: dict[str, str]) -> str:
    """Takes a dictionary of favorite colors and returns the most popular one."""
    frequency: dict[str, int] = {}
    highest_frequency: int = 0
    most_color: str = ""
    for name in info:
        if info[name] in frequency:
            frequency[info[name]] += 1
        else:
            frequency[info[name]] = 1
    for color in frequency:
        if frequency[color] > highest_frequency:
            highest_frequency = frequency[color]
            most_color = color
    return most_color
        

def count(original: list[str]) -> dict[str, int]:
    """Takes a list, and counts the frequency of each item in the list."""
    totals: dict[str, int] = dict()
    i: int = 0
    for item in original:
        if item in totals:
            totals[original[i]] += 1
        else:
            totals[item] = 1
        i += 1
    return totals