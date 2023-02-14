#!/usr/bin/env python3
"""
measures the total execution time
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time (n: int, max_delay: int) -> float:
    """
    returns average runtime
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time 
    return total_time / n
