import asyncio
import time

async def async_sleep(n):
    print("Before Spleep",n)
    n = max(2, n)
    for i in range(1,n):
        yield i
        await asyncio.sleep(i)
    print("After Sleep",n)

async def print_hello():
    print("Hello")

async def main():
    start_time = time.time()
    sum = 0
    async for i in async_sleep(5):
        print(i)
        sum += i
    print("Sum:", sum)
    print("Time Taken:", time.time()-start_time)

if __name__ == "__main__":
    asyncio.run(main())