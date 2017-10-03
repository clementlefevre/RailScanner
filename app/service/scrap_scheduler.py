import schedule
import random
import time
import logging
import sys
from itertools import product, permutations

from app.model.client import Client
from app.config import LOGGING_FILENAME, ALL_TRIPS

logger = logging.getLogger("scraper_sncf")



def job(wait=True):
    if wait:
        wait_times_mn = random.randrange(1, 30, 1)
        time.sleep(wait_times_mn * 60)
    client = Client(ALL_TRIPS, horizon=40)
    client.get_routes()


def main():
    logger.debug("start scheduler...")
    job(wait=False)
    schedule.every(1).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    logger.debug("start scraper...")
    main()
