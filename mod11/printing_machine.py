import logging
import random
import threading
import time

TOTAL_TICKETS = 10
TOTAL_SITS = 80
ESTIMATED_SITS = TOTAL_SITS

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global TOTAL_TICKETS
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self.tickets_sold += 1
                TOTAL_TICKETS -= 1
                logger.info(f'{self.name} sold one; {TOTAL_TICKETS} left')
        logger.info(f'Seller {self.name} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, sellers_count: int):
        super().__init__()
        self.sem = semaphore
        self.sellers_count = sellers_count
        logger.info('Director started work')

    def run(self):
        global TOTAL_TICKETS
        global TOTAL_SITS
        global ESTIMATED_SITS
        while ESTIMATED_SITS > 0:
            if TOTAL_TICKETS <= self.sellers_count:
                with self.sem:
                    addition = self.sellers_count if self.sellers_count < ESTIMATED_SITS else ESTIMATED_SITS % self.sellers_count
                    TOTAL_TICKETS += addition
                    ESTIMATED_SITS -= addition
                    logger.info(f'Director added {addition} tickets. Total tickets: {TOTAL_TICKETS}')



def main():
    semaphore = threading.Semaphore()
    sellers = []
    sellers_count = 8
    director = Director(semaphore=semaphore, sellers_count=sellers_count)
    director.start()
    for _ in range(sellers_count):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()
    director.join()
    logger.info(f'Total sits: {TOTAL_SITS},Estimated sits: {ESTIMATED_SITS},Total tickets: {TOTAL_TICKETS}')


if __name__ == '__main__':
    main()
