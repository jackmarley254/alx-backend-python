#!/usr/bin/env python3
"""This is an Async Generator that yeilds random numbers"""
import asyncio
import random
from typing import Generator


async def async_generator(): -> Generator[float, None, None]:
    """
    async_generator - function to loop 10 times
    Arguments:
        no arguments
    Returns:
        nothing
    """
    for i in range(10)
        await asyncio.sleep(1)
        yield random.randit(0, 10)
