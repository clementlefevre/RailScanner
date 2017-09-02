# TRIPS

TRIP1 = {'origin': 'PARIS', 'destination': [
    'SAINT BRIEUC', 'LYON', 'ANGOULEME', 'LILLE', 'STRASBOURG']}


ALL_TRIPS = [TRIP1]


URL = "https://www.voyages-sncf.com/proposition/rest/search-travels/outward"

headers = {
    'accept': "application/json, text/plain, */*",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.8,de;q=0.6,fr;q=0.4",
    'connection': "keep-alive",
    'content-length': "1049",
    'content-type': "application/json;charset=UTF-8",
    'host': "www.voyages-sncf.com",
    'origin': "https://www.voyages-sncf.com",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    'x-vsd-locale': "fr_FR",
    'cache-control': "no-cache",
}

DB_NAME = 'sncf_trips.db'

LOGGING_PATH = 'scrapper.log'
