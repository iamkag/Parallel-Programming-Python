import asyncio
import time

async def async_sleep(n):
    print("Before Spleep",n)
    await asyncio.sleep(n)
    print("After Sleep",n)

async def print_hello():
    print("Hello")

async def run_1():
    start_time = time.time()
    task = asyncio.create_task(async_sleep(1))
    await async_sleep(2)
    await task
    await print_hello()
    print("Time Taken:", time.time()-start_time)

async def run_2():
    start_time = time.time()
    await asyncio.gather(async_sleep(1), async_sleep(2), print_hello())
    print("Time Taken:", time.time()-start_time)

async def run_3():
    start_time = time.time()
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(30),5), async_sleep(2), print_hello()) #when a server do not response
    except asyncio.TimeoutError:
        print("Timeout Error")
    print("Time Taken:", time.time()-start_time)

if __name__ == "__main__":
    asyncio.run(run_3())