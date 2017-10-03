import logging
import sys
from itertools import product, permutations



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
print 'coucou'