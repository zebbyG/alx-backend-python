#!/usr/bin/env python3
"""
Measure the runtime
"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n
"""
modules required
"""


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the time it takes to run `wait_n`
    return the total average time taken per coroutine
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    stop_time = time.time()
    total_time = stop_time - start_time
    return total_time / n
