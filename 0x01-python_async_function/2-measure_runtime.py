#!/usr/bin/env python3
"""
    A measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay)
    and returns total_time / n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Args: n  - number of times a function will be called in wait_n
              max_delay - a range of random delay with arg being the highest
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elasped = time.perf_counter() - start
    return elasped / n
