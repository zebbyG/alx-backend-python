#!/usr/bin/env python3
"""
Complex types - list of floats
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """
    :param input_list: type-annotated list of floats
    :return: sum of the input_list-float
    """
    return sum(input_list)
