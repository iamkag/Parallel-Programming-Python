import asyncio
import multiprocessing


class MultiprocessingAsync(multiprocessing.Process): 
    def __init__(self, duration):
        super(MultiprocessingAsync, self).__init__()
        self._duration = duration
    
    @staticmethod
    async def async_sleep(duration):
        await asyncio.sleep(duration)
        return duration
    
    async def consecutive_sleeps(self):
        pending = set()
        for duration in self._duration:
            pending.add(asyncio.create_task(self.async_sleep(duration))) # scedule tasks
        
        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, timeout=2) # wait for 2 seconds and then continue
            for task in done:
                print("Task", await task, "done")

    def run(self):
        asyncio.run(self.consecutive_sleeps())
        print("Process", self.name, "is done")

if __name__ == '__main__':
    duration = []   
    for i in range(1, 11):
        duration.append(i)
    processes = []
    for i in range(3):
        processes.append(MultiprocessingAsync(duration[i*5: (i+1)*5])) # 5 tasks for each process
    
    for process in processes:
        process.start()
    
    for process in processes:
        process.join()

    print('This is the end of the program')