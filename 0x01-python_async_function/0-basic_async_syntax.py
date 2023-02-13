#!/usr/bin/env python3
""" Basics of async """


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for a random delay and return 
    """
    ran_time = max_delay * random.random()
    await asyncio.sleep(ran_time)
    return ran_time
