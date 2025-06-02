import asyncio
import time
import requests
import aiohttp


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def get_url_response2(url):
        return requests.get(url).text # no await event to give controlo to the event loop

async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/requests/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://medium.com']

    # Sync requests
    start = time.time()
    sync_text_response = []
    for url in urls:
        sync_text_response.append(requests.get(url).text)

    end_time = time.time()
    print('Requests time:', end_time - start)

    # Wrong async requests
    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response2(url)))
    
    sync_text_response = await asyncio.gather(*tasks)

    end_time = time.time()
    print('Requests time:', end_time - start)

    # Async requests
    start_async = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    end_time_async = time.time()
    print('Async requests time:', end_time_async - start_async)


if __name__ == '__main__':
    asyncio.run(main())