import schedule
import random
import time
import logging
import sys
from itertools import product, permutations

from app.config import LOGGING_PATH, ALL_TRIPS

from app.model.trips import Trips
from app.service.sncf_routes import get_data


logging.basicConfig(filename=LOGGING_PATH, level=logging.DEBUG)
logger = logging.getLogger("scraper_sncf")


def job():
    wait_times_mn = random.randrange(1, 58, 1)

    #time.sleep(wait_times_mn * 60)
    trips = Trips(ALL_TRIPS)
    print trips.legs
    for leg in trips.legs:
        get_data(leg[0], leg[1])


def main():
    logger.debug("start working...")
    job()
    schedule.every(4).hours.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':

    print LOGGING_PATH

    main()
