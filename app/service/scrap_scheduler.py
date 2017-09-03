import schedule
import random
import time
import logging
import sys
from itertools import product, permutations

import ipdb

#ipdb.set_trace()

from app.model.client import Client
from app.config import LOGGING_FILENAME, ALL_TRIPS


logFormatter = logging.Formatter(
    "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger("scraper_sncf")
rootLogger.setLevel(logging.INFO)

fileHandler = logging.FileHandler(
    "{0}/{1}.log".format("app/logs", LOGGING_FILENAME))
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)


def job(wait=True):
    if wait:
        wait_times_mn = random.randrange(1, 58, 1)
        time.sleep(wait_times_mn * 60)
    client = Client(ALL_TRIPS, horizon=40)
    client.get_routes()


def main():
    rootLogger.debug("start scheduler...")
    job(wait=False)
    schedule.every(4).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    
    
    rootLogger.debug("start scraper...")
    main()
