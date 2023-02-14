#!/usr/bin/env python3
"""
wait like function
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_with_random(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n  addtimes with the specified max_delay
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
