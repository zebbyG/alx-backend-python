#!/usr/bin/env python3
"""
Task 4's module.
"""
# import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    :return: a list of all the delays
    """
    list_of_delays = []
    for i in range(n):
        delay1 = await wait_random(max_delay)
        # list_of_delays.append(delay1)
        delay2 = await task_wait_random(max_delay)
        # list_of_delays.append(delay2)
        delays = delay1 + delay2
        list_of_delays.append(delays)
    return sorted(list_of_delays)
