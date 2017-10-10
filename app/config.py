import os

# TRIPS

TRIP1 = {'origin': 'PARIS', 'destination': ['NANTES','LILLE','LYON','BORDEAUX','STRASBOURG',
    'SAINT BRIEUC']}


ALL_TRIPS = [TRIP1]


# PROXIES

PROXIES = ['62.210.94.215:80','78.193.56.236:8118','88.170.1.143:8118','83.206.37.227:80','80.14.12.161:80','85.31.205.178:80','193.105.216.91:80',
'193.107.19.161:3128',
'89.31.150.71:8080',
'80.15.214.252:3128',
'91.121.14.55:80',
'212.47.239.175:8080',
'195.154.75.114:3128',
'212.47.237.189:3128',
'217.151.3.79:80',
    '83.177.139.91:9064']

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
