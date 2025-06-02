import asyncio

async def async_sleep(duration):
    await asyncio.sleep(duration)
    return duration

async def main():
    pending = set ()
    for i in range(1, 11):
        pending.add(asyncio.create_task(async_sleep(i)))
    

    add_task = True
    while len(pending) > 0:
        # done, pending = await asyncio.wait(pending, timeout=2) # wait for 2 seconds and then continue
        done, pending = await asyncio.wait(pending, return_when= 'FIRST_COMPLETED') # wait for the first task to complete and then continue
        print("#####")
        for task in done:
            print("Task", await task, "done") # with await we can get the result of the task (duration)
        print("#####")

        if add_task:
            print("&&&&&&&&&&&&")
            print("Adding a new task")
            pending.add(asyncio.create_task(async_sleep(5)))
            add_task = False
            print("&&&&&&&&&&&&")


if __name__ == '__main__':
    asyncio.run(main())
    print('This is the end of the program')