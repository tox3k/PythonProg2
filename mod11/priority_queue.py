import datetime
import random
import threading, queue
import logging

QUEUE = queue.PriorityQueue()

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)

def task():
    difficult = random.randint(5, 8)
    res = 0
    for i in range(difficult):
        res += difficult**difficult**difficult


class Producer(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, tasks_count: int):
        super().__init__()
        self.sem = semaphore
        self.tasks_count = tasks_count
        logger.info('Producer started.')

    def run(self):
        with self.sem:
            global QUEUE
            for i in range(self.tasks_count):
                QUEUE.put((random.randint(0, 5), task))


class Consumer(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        logger.info('Consumer started.')

    def run(self):
        startRun = datetime.datetime.now()
        global QUEUE
        with self.sem:
            while not QUEUE.empty():
                start = datetime.datetime.now()
                res = QUEUE.get()[1]
                res()
                QUEUE.task_done()
                logger.info(f'Task done! Elapsed time: {datetime.datetime.now() - start}')

        logger.info(f'Queue done in {datetime.datetime.now() - startRun} seconds.')



def main():
    semaphore = threading.Semaphore()
    prod = Producer(semaphore=semaphore, tasks_count=15)
    prod.start()
    cons = Consumer(semaphore=semaphore)
    cons.start()
    prod.join()
    cons.join()

if __name__ == '__main__':
    main()
