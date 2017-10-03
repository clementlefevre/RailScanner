import os

# TRIPS

TRIP1 = {'origin': 'PARIS', 'destination': [
    'SAINT BRIEUC']}


ALL_TRIPS = [TRIP1]


# PROXIES
PROXIES = ['176.31.125.111:80',
           '81.49.137.110:80',
           '46.105.132.60:8118',
           '213.163.181.33:80',
           '51.255.161.222:80',
           '88.170.1.143:8118',
           '134.119.223.242:80',
           '159.8.114.37:25',
           '159.8.114.37:8123',
           '89.145.177.26:8080',
           '46.218.73.162:80',
           '163.172.59.200:8080',
           '137.74.254.198:3128',
           '178.33.62.155:8118',
           '62.210.51.150:80',
           '151.80.37.154:3128',
           '178.32.213.128:80']


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

LOGGING_FILENAME = 'scrapper'

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
MAIL_SERVER = 'smtp.world4you.com'
MAIL_PORT = 587
MAIL_SENDER = 'Railscanner Admin <flask.admin@lefevre.at>'
