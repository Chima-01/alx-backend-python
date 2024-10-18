#!/usr/bin/env python3
"""
Code from wait_n and altered to a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random called.
"""
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    task = await wait_n(n, max_delay)
    return task
