#!/usr/bin/env python3
"""
Async Comprehensions
"""


import typing

async_generator = __import__('0-async_generator').async_generator
"""
modules required
"""


async def async_comprehension() -> typing.List[float]:
    """ Return list of values yielded by async_generator."""
    return [value async for value in async_generator()]
