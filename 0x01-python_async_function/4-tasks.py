#!/usr/bin/env python3
"""
Code from wait_n and altered to a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n - number of times to call coroutine
        max_delay - Delay time
    """
    task = [task_wait_random(max_delay) for _ in range(n)]
    all_task = await asyncio.gather(*task)
    return sorted(all_task)
