import logging
import threading
import random
import time

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock):
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def dining(self):
        logger.info(f'Philosopher {self.name} starts eating.')
        time.sleep(random.randint(1, 10))
        logger.info(f'Philosopher {self.name} finishes eating and leaves to think.')

    def run(self):
        while self.running:
            logger.info(f'Philosopher {self.name} start thinking.')
            time.sleep(random.randint(1, 10))
            logger.info(f'Philosopher {self.name} is hungry.')
            with self.left_fork:
                logger.info(f'Philosopher {self.name} acquired left fork')
                if self.right_fork.locked():
                    continue

                with self.right_fork:
                    logger.info(f'Philosopher {self.name} acquired right fork')
                    self.dining()


def main():
    forks = [threading.Lock() for n in range(5)]
    philosophers = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5])
        for i in range(5)
    ]

    Philosopher.running = True
    for p in philosophers:
        p.start()
    time.sleep(200)
    Philosopher.running = False
    logger.info('Now we\'re finishing.')


if __name__ == '__main__':
    main()
