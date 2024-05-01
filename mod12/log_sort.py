import threading
from threading import Semaphore
import time
from datetime import datetime, timedelta, tzinfo
import requests
import logging
URL = 'http://127.0.0.1:5000/timestamp/'
sem: Semaphore = Semaphore()

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, filename=f'{__name__}.log', filemode='w')
STOP_LOGGING = False

def log_data():
    start = datetime.now()
    while True:
        if datetime.now() - start > timedelta(seconds=20):
            break

        with sem:
            global URL
            timestamp = datetime.timestamp(datetime.now())
            date = requests.get(URL + str(timestamp)).text
            logger.info(f'Timestamp: {timestamp : .3f}\t\tDate: {date}')
        time.sleep(1)

def main():
    threads = [threading.Thread(target=log_data) for _ in range(10)]
    for thread in threads:
        thread.start()
        time.sleep(1)

if __name__ == '__main__':
    main()