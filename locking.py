import threading

counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(10**7):
        # lock.acquire()
        with lock:
            counter +=  1
        # lock.release()

threads = []

for i in range(4):
    thread = threading.Thread(target=increment)
    threads.append(thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(f"Counter: {counter}")