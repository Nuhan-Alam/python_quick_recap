# Python Recap: Asynchronous Programming (asyncio)

import asyncio
import time
from typing import List

# ===== BASIC ASYNC/AWAIT =====

# 1. Simple async function
async def greet():
    return "Hello, Async World!"

async def example_1():
    result = await greet()
    print(f"1. Simple async function: {result}")

asyncio.run(example_1())
print()

# 2. async function with delay
async def say_after(delay, message):
    await asyncio.sleep(delay)
    return message

async def example_2():
    print("2. Async with delay:")
    start = time.time()
    result = await say_after(1, "Hello after 1 second")
    print(f"   {result}")
    print(f"   Time taken: {time.time() - start:.2f}s")

asyncio.run(example_2())
example_2() # will through error " coroutine 'example_2' was never awaited"
# Because coroutine can't run except inside event loop
# Coroutine is similar to JS promise but not similar, it just creates an object
print()

# 3. Running multiple coroutines sequentially
async def task_a():
    await asyncio.sleep(1)
    return "Task A done"

async def task_b():
    await asyncio.sleep(1)
    return "Task B done"

async def example_3():
    print("3. Sequential execution:")
    start = time.time()
    result_a = await task_a()
    result_b = await task_b()
    print(f"   {result_a}, {result_b}")
    print(f"   Time taken: {time.time() - start:.2f}s (sequential)")

asyncio.run(example_3())
print()

# ===== CONCURRENT EXECUTION =====

# 4. asyncio.gather() - run multiple coroutines concurrently
async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    return f"Data {id}"

async def example_4():
    print("4. asyncio.gather() - concurrent:")
    start = time.time()
    results = await asyncio.gather(
        fetch_data(1, 1),
        fetch_data(2, 2),
        fetch_data(3, 1)
    )
    print(f"   Results: {results}")
    print(f"   Time taken: {time.time() - start:.2f}s (concurrent)")

asyncio.run(example_4())
print()

# 5. asyncio.create_task() - schedule coroutines
async def example_5():
    print("5. create_task() - background tasks:")
    start = time.time()
    
    # Doesn't await Automatically like asyncio.gather()
    task1 = asyncio.create_task(fetch_data(1, 1))
    task2 = asyncio.create_task(fetch_data(2, 2))
    task3 = asyncio.create_task(fetch_data(3, 1))
    
    # You can do some other stuffs in the middle first
    
    # Awaits now
    result1 = await task1
    result2 = await task2
    result3 = await task3
    
    print(f"   Results: {result1}, {result2}, {result3}")
    print(f"   Time taken: {time.time() - start:.2f}s")

asyncio.run(example_5())
print()

# 6. asyncio.wait() - wait for tasks with different strategies
async def example_6():
    print("6. asyncio.wait() - wait for first completed:")
    
    tasks = [
        asyncio.create_task(fetch_data(1, 2)),
        asyncio.create_task(fetch_data(2, 1)),
        asyncio.create_task(fetch_data(3, 3))
    ]
    
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    print(f"   First completed: {[task.result() for task in done]}")
    print(f"   Still pending: {len(pending)} tasks")
    
    # Cancel pending tasks
    for task in pending:
        task.cancel()

asyncio.run(example_6())
print()

# ===== ASYNC GENERATORS AND ITERATORS =====

# 7. Async generator
async def async_counter(max_count):
    for i in range(max_count):
        await asyncio.sleep(0.1)
        yield i

async def example_7():
    print("7. Async generator:")
    async for num in async_counter(5):
        print(f"   Count: {num}")

asyncio.run(example_7())
print()

# 8. Async comprehension
async def example_8():
    print("8. Async comprehension:")
    results = [i async for i in async_counter(5)]
    print(f"   Results: {results}")

asyncio.run(example_8())
print()

# 9. Async iterator (custom)
class AsyncRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.current >= self.end:
            raise StopAsyncIteration
        await asyncio.sleep(0.1)
        value = self.current
        self.current += 1
        return value

async def example_9():
    print("9. Custom async iterator:")
    async for num in AsyncRange(0, 5):
        print(f"   Number: {num}")

asyncio.run(example_9())
print()

# ===== ASYNC CONTEXT MANAGERS =====
print("--- ASYNC CONTEXT MANAGERS ---\n")

# 10. Async context manager
class AsyncResource:
    async def __aenter__(self):
        print("   Acquiring resource...")
        await asyncio.sleep(0.5)
        print("   Resource acquired")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("   Releasing resource...")
        await asyncio.sleep(0.5)
        print("   Resource released")

async def example_10():
    print("10. Async context manager:")
    async with AsyncResource() as resource:
        print("   Using resource")

asyncio.run(example_10())
print()

# ===== ERROR HANDLING =====
print("--- ERROR HANDLING ---\n")

# 11. Exception handling in async
async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong!")

async def example_11():
    print("11. Exception handling:")
    try:
        await failing_task()
    except ValueError as e:
        print(f"   Caught exception: {e}")

asyncio.run(example_11())
print()

# 12. gather with return_exceptions
async def task_that_fails():
    await asyncio.sleep(0.5)
    raise Exception("Task failed")

async def task_that_succeeds():
    await asyncio.sleep(0.5)
    return "Success"

async def example_12():
    print("12. gather with return_exceptions=True:")
    results = await asyncio.gather(
        task_that_succeeds(),
        task_that_fails(),
        return_exceptions=True
    )
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"   Task {i}: Exception - {result}")
        else:
            print(f"   Task {i}: {result}")

asyncio.run(example_12())
print()

# ===== TIMEOUTS AND CANCELLATION =====
print("--- TIMEOUTS AND CANCELLATION ---\n")

# 13. asyncio.wait_for() with timeout
async def long_task():
    await asyncio.sleep(3)
    return "Done"

async def example_13():
    print("13. Timeout with wait_for():")
    try:
        result = await asyncio.wait_for(long_task(), timeout=1.0)
        print(f"   Result: {result}")
    except asyncio.TimeoutError:
        print("   Task timed out!")

asyncio.run(example_13())
print()

# 14. Manual task cancellation
async def cancellable_task():
    try:
        print("   Task started")
        await asyncio.sleep(5)
        print("   Task completed")
    except asyncio.CancelledError:
        print("   Task was cancelled")
        raise

async def example_14():
    print("14. Manual cancellation:")
    task = asyncio.create_task(cancellable_task())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("   Confirmed: Task cancelled")

asyncio.run(example_14())
print()

# ===== SYNCHRONIZATION PRIMITIVES =====
print("--- SYNCHRONIZATION PRIMITIVES ---\n")

# 15. asyncio.Lock
shared_resource = 0
lock = asyncio.Lock()

async def increment_with_lock():
    global shared_resource
    async with lock:
        temp = shared_resource
        await asyncio.sleep(0.1)
        shared_resource = temp + 1

async def example_15():
    global shared_resource
    shared_resource = 0
    print("15. Lock for synchronization:")
    await asyncio.gather(*[increment_with_lock() for _ in range(5)])
    print(f"   Final value: {shared_resource}")

asyncio.run(example_15())
print()

# 16. asyncio.Semaphore
async def limited_task(sem, id):
    async with sem:
        print(f"   Task {id} running")
        await asyncio.sleep(1)
        print(f"   Task {id} done")

async def example_16():
    print("16. Semaphore (limit concurrent tasks):")
    sem = asyncio.Semaphore(2)  # Only 2 concurrent tasks
    await asyncio.gather(*[limited_task(sem, i) for i in range(5)])

asyncio.run(example_16())
print()

# 17. asyncio.Event
async def waiter(event, name):
    print(f"   {name} waiting for event...")
    await event.wait()
    print(f"   {name} received event!")

async def setter(event):
    await asyncio.sleep(2)
    print("   Setting event...")
    event.set()

async def example_17():
    print("17. Event for signaling:")
    event = asyncio.Event()
    await asyncio.gather(
        waiter(event, "Waiter 1"),
        waiter(event, "Waiter 2"),
        setter(event)
    )

asyncio.run(example_17())
print()

# ===== QUEUES =====
print("--- QUEUES ---\n")

# 18. asyncio.Queue
async def producer(queue, id):
    for i in range(3):
        await asyncio.sleep(0.5)
        item = f"Item-{id}-{i}"
        await queue.put(item)
        print(f"   Producer {id} produced: {item}")

async def consumer(queue, id):
    while True:
        item = await queue.get()
        print(f"   Consumer {id} consumed: {item}")
        await asyncio.sleep(1)
        queue.task_done()

async def example_18():
    print("18. Queue (producer-consumer):")
    queue = asyncio.Queue()
    
    producers = [asyncio.create_task(producer(queue, i)) for i in range(2)]
    consumers = [asyncio.create_task(consumer(queue, i)) for i in range(2)]
    
    await asyncio.gather(*producers)
    await queue.join()
    
    for c in consumers:
        c.cancel()

asyncio.run(example_18())
print()

# ===== RUNNING BLOCKING CODE =====
print("--- RUNNING BLOCKING CODE ---\n")

# 19. run_in_executor() for CPU-bound tasks
def blocking_io():
    time.sleep(1)
    return "Blocking IO done"

async def example_19():
    print("19. run_in_executor() for blocking code:")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, blocking_io)
    print(f"   {result}")

asyncio.run(example_19())
print()

# ===== TASK GROUPS (Python 3.11+) =====
print("--- TASK GROUPS (Python 3.11+) ---\n")

# 20. TaskGroup for structured concurrency
async def example_20():
    print("20. TaskGroup (Python 3.11+):")
    try:
        async with asyncio.TaskGroup() as tg:
            task1 = tg.create_task(fetch_data(1, 1))
            task2 = tg.create_task(fetch_data(2, 1))
        print(f"   Results: {task1.result()}, {task2.result()}")
    except AttributeError:
        print("   TaskGroup not available (requires Python 3.11+)")

asyncio.run(example_20())
print()

# ===== ASYNC WITH CALLBACKS =====
print("--- ASYNC WITH CALLBACKS ---\n")

# 21. Futures and callbacks
async def example_21():
    print("21. Future with callback:")
    
    def callback(future):
        print(f"   Callback called with result: {future.result()}")
    
    future = asyncio.Future()
    future.add_done_callback(callback)
    
    await asyncio.sleep(1)
    future.set_result("Future result")
    await asyncio.sleep(0.1)  # Give callback time to execute

asyncio.run(example_21())
print()

# ===== PRACTICAL EXAMPLE: WEB SCRAPING SIMULATION =====
print("--- PRACTICAL EXAMPLE ---\n")

# 22. Simulated concurrent web requests
async def fetch_url(url, delay):
    print(f"   Fetching {url}...")
    await asyncio.sleep(delay)
    return f"Content from {url}"

async def example_22():
    print("22. Concurrent web requests (simulated):")
    start = time.time()
    
    urls = [
        ("url1.com", 1),
        ("url2.com", 2),
        ("url3.com", 1),
        ("url4.com", 1.5)
    ]
    
    results = await asyncio.gather(*[fetch_url(url, delay) for url, delay in urls])
    
    print(f"   Fetched {len(results)} URLs")
    print(f"   Time taken: {time.time() - start:.2f}s (vs ~5.5s sequential)")

asyncio.run(example_22())
print()

# ===== ASYNC CLASS METHODS =====
print("--- ASYNC CLASS METHODS ---\n")

# 23. Class with async methods
class AsyncDatabase:
    def __init__(self):
        self.data = {}
    
    async def connect(self):
        print("   Connecting to database...")
        await asyncio.sleep(1)
        print("   Connected!")
    
    async def insert(self, key, value):
        await asyncio.sleep(0.5)
        self.data[key] = value
        return f"Inserted {key}"
    
    async def fetch(self, key):
        await asyncio.sleep(0.3)
        return self.data.get(key, "Not found")

async def example_23():
    print("23. Async class methods:")
    db = AsyncDatabase()
    await db.connect()
    await db.insert("user1", "Alice")
    result = await db.fetch("user1")
    print(f"   Fetched: {result}")

asyncio.run(example_23())
print()

print("="*60)
print("END OF ASYNC PROGRAMMING CONCEPTS")
print("="*60)