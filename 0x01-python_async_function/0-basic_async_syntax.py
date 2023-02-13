#!/usr/bin/env python3
"""
COntains coroutine wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay
    and eventually returns it
    """
    ran_time = max_delay * random.random()
    await asyncio.sleep(ran_time)
    return ran_time
