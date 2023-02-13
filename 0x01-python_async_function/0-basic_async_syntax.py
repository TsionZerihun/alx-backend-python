#!/usr/bin/env python3
"""
COntains coroutine wait_random
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits random delay between 0 and max_delay
    and returns it
    """
    wait_time = max_delay * random.random()
    await asyncio.sleep(wait_time)
    return wait_time
