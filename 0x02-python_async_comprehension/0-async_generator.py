#!/usr/bin/env python3
"""
coroutine function
"""
import asyncio
import random
from typing import Generator


async def async_generato() -> Generator[float, None, None]:
    '''
    yield a random number between 0 and 10
    '''
    async for _ in range(10):
        await asyncio.sleep(1)
        yield random.rand() * 10