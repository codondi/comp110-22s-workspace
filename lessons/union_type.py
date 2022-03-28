"""An example of Union types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """log is a function that can be called with either a str or int argument."""
    if isinstance(info, str):
        print(f"str: {info.lower}")
    else:
        print(f"int: {info}")


log("Hello, World")
log(110)