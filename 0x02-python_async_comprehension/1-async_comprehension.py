#!/usr/bin/env python3
"""
Async Comprehensions
"""


import typing
import asyncio
import random
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    return [value async for value in async_generator()]
