#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random
"""
modules required for task
"""


async def wait_random(max_delay: int = 10) -> float:
    """
    :param max_delay: delay time range
    :return: the delay time for output
    """
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
