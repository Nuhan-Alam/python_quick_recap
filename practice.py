import asyncio
import time

# 4. asyncio.gather() - run multiple coroutines concurrently
async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    return f"Data {id}"


async def async_counter(max_count):
    for i in range(max_count):
        await asyncio.sleep(2)
        yield i

# 8. Async comprehension
async def example_8():
    print("8. Async comprehension:")
    results = [i async for i in async_counter(5)]
    print(f"   Results: {results}")

asyncio.run(example_8())
print()