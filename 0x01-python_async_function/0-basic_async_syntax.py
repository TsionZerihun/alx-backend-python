#!/usr/bin/env python3
""" Basic syntax await async """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random delay and returns 
    """
    wait_time = max_delay * random.random()
    await asyncio.sleep(wait_time)
    return wait_time
