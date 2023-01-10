#!/usr/bin/env python3
"""
Async Generator
"""

import asyncio
import random
import typing
"""
modules required for task
"""


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Yield numbers from 0 to 10 every *delay* seconds.
    """
    for z in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
