#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import json
import pandas as pd
from sqlalchemy import create_engine
import requests
from datetime import datetime
import logging
from random import choice


from app.config import URL, headers, DB_NAME, PROXIES


logger = logging.getLogger("scraper_sncf")

import ipdb

COLS_PRICE = ['price_FLEX', 'price_NOFLEX', 'price_SEMIFLEX', 'price_UPSELL']
COLS_DATE = ['departureDate', 'arrivalDate',
             'trip_departureDate', 'trip_arrivalDate', 'scrapped_on']

COLS_TIMEDELTA = ['total_duration']


def get_proxy():
    return choice(PROXIES)


def get_data(origin, destination, date_trip=datetime.now().isoformat()):

    null = 'null'
    false = 'false'
    true = 'true'
    BIKE ='UNFOLDABLE'
    BIKE = 'NONE'

    payload = {"origin": origin, "originCode": null,
               "originLocation": null, "destination": destination,
               "destinationCode": null, "destinationLocation": null,
               "directTravel": false, "asymmetrical": false,
               "professional": false,
               "customerAccount": false, "oneWayTravel": true,
               "departureDate": date_trip, "returnDate": null,
               "travelClass": "SECOND", "country": "FR", "language": "fr",
               "busBestPriceOperator": null, "busOnly": false, "passengers": [
                   {"travelerId": null, "profile": "ADULT",
                    "age": 26, "birthDate": null, "fidelityCardType": "NONE",
                    "fidelityCardNumber": null, "commercialCardNumber": null,
                    "commercialCardType": "NONE", "promoCode": "",
                    "lastName": null,
                    "firstName": null, "phoneNumer": null,
                    "hanInformation": null}],
               "animals": [], "bike":BIKE, "withRecliningSeat": false,
               "physicalSpace": null, "fares": [], "withBestPrices": false,
               "highlightedTravel": null, "nextOrPrevious": false,
               "source": "FORM_SUBMIT", "targetPrice": null, "han": false,
               }

    payload = json.dumps(payload)
    payload = payload.replace("\"null\"", "null").replace(
        "\"false\"", "false").replace("\"true\"", "true")
    return payload


def add_min_price(df):
    price_cols = [col for col in df.columns if 'price' in col]
    df['min_price'] = df[price_cols].min(skipna=True, axis=1)
    return df


def add_scraping_timestamp(df):
    df['scrapped_on'] = datetime.now().isoformat()
    return df


def add_missing_cols_price(df):
    for col in COLS_PRICE:
        if col not in df:
            df[col] = None
            df[col] = pd.to_numeric(df[col])

    return df


def get_routes(origin, destination, date_trip=datetime.now().isoformat()):
    data = get_data(origin, destination, date_trip)
    time.sleep(20)
    proxy = get_proxy()

    try:
        session = requests.Session()
        
        proxies = {'http': str(proxy)}
        logger.info('Using proxy : {}'.format(proxies))
        session.proxies.update(proxies)
        #logger.info('IP in use : {}'.format(session.get("http://httpbin.org/ip").text))
        response = session.request("POST", URL, data=data, headers=headers, timeout=20)
        #response = requests.request("POST", URL, data=data, headers=headers)
        response.raise_for_status()
    except Exception as e:
        logger.error(
            "Could not get schedule for {0}-{1} on {2}: ".format(origin, destination, date_trip))
        
        logger.error(e)
        try:
            logger.error('response text :{}'.format(response.text))
        except UnboundLocalError:
            logger.error('No response for {}'.format(proxy))
        

        return

    response_dict = response.json()

    result_list = response_dict['results']

    logger.info(
        "Itineraries found for {0}-{1} on {2}: {3}\n".format(origin, destination, date_trip, len(result_list)))
    df = concat_results(result_list)
    df = add_min_price(df)

    df = add_scraping_timestamp(df)

    return df


def convert_result_to_dataframe(result):

    df = pd.DataFrame()

    df = pd.DataFrame.from_records(result['segments'])

    # ipdb.set_trace()
    if result['pushProposalType'] == 'BUS':
        # print "BUS"
        return

    # if result['unsellableReason'] == "FULL_TRAIN":
    #     print "FULL TRAIN"
    #     return

    if 'CAR' in df.trainType.values:
        # print "AUTOCAR"
        return

    # if np.sum(df.trainType != 'TER') > 0:
    #     print "NOT ONLY TER"
    #     return

    df[['departureDate', 'arrivalDate']] = df[['departureDate', 'arrivalDate']
                                              ].applymap(lambda x: pd.to_datetime(x, format="%Y-%m-%dT%H:%M:%S"))
    df['total_duration'] = df['arrivalDate'].iloc[-1] - \
        df['departureDate'].iloc[0]
    df['trip_name'] = u' to '.join([result['origin'], result['destination']])
    df['trip_id'] = result['id']
    df['unsellableReason'] = result['unsellableReason']
    df['has_TGV'] = 'TGV' in df['transporter'].values
    df['total_trains'] = df.shape[0]
    df['trip_rank'] = df.index
    df['trip_departureDate'] = result['departureDate']
    df['trip_arrivalDate'] = result['arrivalDate']
    #df['trainNumber'] = result['trainNumber']

    for price_key in result['priceProposals'].keys():
        df[''.join(["price_", price_key])] = result[
            'priceProposals'][price_key]['amount']

    return df


def save_to_db(df):

    df = add_missing_cols_price(df)

    df = df[['has_TGV',  'destination', 'destinationCode', 'duration', 'min_price',
             'origin', 'originCode',  'total_duration',
             'total_trains', 'trainNumber', 'trainPeriod', 'trainType', 'trainNumber',  'transporter',
             'trip_id', 'trip_name',  'trip_rank',
             'vehicleType'] + COLS_TIMEDELTA + COLS_DATE + COLS_PRICE]
    disk_engine = create_engine('sqlite:///' + DB_NAME)
    logger.info("Start writing to db...")
    df.to_sql('sncf_trips', disk_engine, if_exists='append')
    logger.info("finished writing to db")


def read_from_db():
    disk_engine = create_engine('sqlite:///' + DB_NAME)
    df = pd.read_sql_query('SELECT * FROM sncf_trips',
                           disk_engine, parse_dates=COLS_DATE)

    df[COLS_TIMEDELTA] = df[COLS_TIMEDELTA].applymap(
        lambda x: pd.to_timedelta(x))
    return df


def convert_date_to_string(df):
    df[COLS_DATE + COLS_TIMEDELTA] = df[COLS_DATE + COLS_TIMEDELTA].applymap(
        lambda x: str(x))
    return df


def concat_results(json_result):
    df = pd.DataFrame()

    for result in json_result:

        try:
            df_result = convert_result_to_dataframe(result)

            df = pd.concat([df, df_result], axis=0)
        except Exception as e:

            print ("error rootacause : \n \n", e.args)
    return df
