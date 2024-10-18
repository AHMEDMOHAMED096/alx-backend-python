#!/usr/bin/env python3
"""import required modules"""
import asyncio
import random


async def async_generator():
    """An asynchronous generator that yields random numbers."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
