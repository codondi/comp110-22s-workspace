"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union
# from xxlimited import new

__author__ = "730449161"


class Simpy:
    """Simpy library."""
    values: list[float] = []

    def __init__(self, values: list[float]):
        """Function for name."""
        self.values = values

    def __str__(self) -> str: 
        """Function for representation."""
        return f"Simpy({self.values})"

    def fill(self, number: float, amount: int) -> None:
        """Fills in values a given number of times."""
        self.values = []
        for i in range(amount):
            self.values.append(number)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a range of values between two values, with a given incrementation."""
        assert step != 0.0
        assert (step > 0 and start < stop) or (step < 0 and start > stop)
        if step < 0.0:
            while start > stop:
                self.values.append(start)
                start += step
            step = 1
        if step > 0.0:
            while start < stop:
                self.values.append(start)
                start += step
            step = 1

    def sum(self) -> float:
        """Adds up values."""
        return sum(self.values)

    def __add__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Adds values by a given number."""
        result = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(rhs.values) == len(self.values)
            while i < len(self.values):
                result.append(self.values[i] + rhs.values[i])
                i += 1
            # for i in range(len(self.values)):
            #     result.values.append(self.values[i] + rhs.values[i])
        else:
            # for i in self.values:
            #     result.values.append(i + rhs)
            while i < len(self.values):
                result.append(self.values[i] + rhs)
                i += 1
        return Simpy(result)

    def __pow__(self, rhs: Union[Simpy, float]) -> Simpy:
        """Raises values to a given power."""
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            new_Simpy = Simpy([])
            for i in range(len(self.values)):
                new_Simpy.values.append(self.values[i] ** rhs.values[i])
            return new_Simpy
        if isinstance(rhs, float):
            other_new_Simpy = Simpy([])
            for i in self.values:
                other_new_Simpy.values.append(i ** rhs)
            return other_new_Simpy

    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Checks values that are equal."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        if isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] == rhs)
                i += 1
        
        return result

    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Creates a mask."""
        result: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        if isinstance(rhs, float):
            while i < len(self.values):
                result.append(self.values[i] > rhs)
                i += 1
        
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets items that pass mask test."""
        result: Simpy = Simpy([])
        i: int = 0
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            assert len(self.values) == len(rhs)
            while i < len(self.values):
                if rhs[i]:
                    result.values.append(self.values[i])
                i += 1
        return result