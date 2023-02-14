##!/usr/bin/env python3
"""
measure time function
"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    calcualte and return toal time
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_time = time.time() - start_time
    return (total_time)