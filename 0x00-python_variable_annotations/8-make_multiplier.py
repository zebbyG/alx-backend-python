#!/usr/bin/env python3
"""
Complex types - functions
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    :param multiplier: is a float
    :return a function that multiplies multiplier by a float
    """
    def num_multiplier(num: float) -> float:
        """
        :param num: a float to be multiplied by multiplier
        :return: float(multiplier * num)
        """
        return multiplier * num
    return num_multiplier
