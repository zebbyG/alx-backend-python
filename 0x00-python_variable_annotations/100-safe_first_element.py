#!/usr/bin/env python3
"""Description: Augment the following code with the correct
                 duck-typed annotations
    Arguments: lst: Sequence[Any]"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> typing.Union[typing.Any, None]:
    """Return the first element of lst if there is any, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
