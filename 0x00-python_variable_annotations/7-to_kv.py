#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    param k:annotated string
    :param v:annotated int or float
    :return:a Tuple(string k as first element
    """
    return k, v ** 2
