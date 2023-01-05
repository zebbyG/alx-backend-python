#!/usr/bin/env python3
"""
 Complex types - mixed list
"""

import typing
"""
to help static type checkers and linters accurately predict errors.
"""


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    :param mxd_lst: a list of integers
    :return: their sum as a float
    """
    return sum(mxd_lst)
