#!/usr/bin/env python3
"""
asynchronous coroutine using random delay
"""


import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random delay and Return 
    """
    ran_time = max_delay * random.random()
    await asyncio.sleep(ran_time)
    return ran_time
