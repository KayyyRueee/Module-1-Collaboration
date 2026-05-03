import multiprocessing
import random
import time
from datetime import datetime

def worker():
    wait_time = random.random()
    time.sleep(wait_time)

    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=worker)
    p2 = multiprocessing.Process(target=worker)
    p3 = multiprocessing.Process(target=worker)
    
    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()