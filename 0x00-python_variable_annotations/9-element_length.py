#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""

import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    :param lst:
    :return: a list of tuples with the length of each element
    """
    return [(i, len(i)) for i in lst]
