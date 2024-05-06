#!/usr/bin/env python3
"""
This is a coroutine taking optional argument and uses random
module to generate a random delay.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """ 
    Returns a random float between 0 and max_delay
    Args:
        max_delay: The maximum delay to return
    Returns:
        A random float between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

#print(asyncio.run(wait_random()))
#print(asyncio.run(wait_random(5)))
#print(asyncio.run(wait_random(15)))
