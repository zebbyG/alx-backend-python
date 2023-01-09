#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random
"""
required imports for task
"""


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    :return: a list of all the delays
    """
    list_of_delays = []
    for i in range(n):
        delays = await wait_random(max_delay)
        list_of_delays.append(delays)
    return sorted(list_of_delays)
