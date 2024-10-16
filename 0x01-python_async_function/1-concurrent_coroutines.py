#!/usr/bin/env python3
"""
    A function spawn wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        args: n - spawn `wait_random` n times
              max_delay - delay time for wait_random
    """
    result = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    result.sort()
    return result
