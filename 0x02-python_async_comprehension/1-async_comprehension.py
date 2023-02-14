##!/usr/bin/env python3
"""
imports from task0
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Returts list of yiled
    """
    return ([yiled_item async for yiled_item in async_generator])