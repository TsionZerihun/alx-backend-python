#!/usr/bin/env python3
""" 
Basic syntax await async wait_random
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        Args:
            max_delay: max wait
        Return:
            float time random
    """ 
    wait_time = max_delay * random.random()
    await asyncio.sleep(wait_time)
    return wait_time
