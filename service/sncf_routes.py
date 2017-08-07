# coding: utf-8

import time
import json
import pandas as pd
import requests
from datetime import datetime
import pprint


#import ipdb


from config import URL, headers


def get_data(origin="Aurillac", destination="Brive la Gaillarde", date_trip=datetime.now().isoformat()):

    null = 'null'
    false = 'false'
    true = 'true'

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
               "animals": [], "bike": "NONE", "withRecliningSeat": false,
               "physicalSpace": null, "fares": [], "withBestPrices": false,
               "highlightedTravel": null, "nextOrPrevious": false,
               "source": "FORM_SUBMIT", "targetPrice": null, "han": false,
               "$initial": true, "$queryId": "SRlEN"}

    payload = json.dumps(payload)
    payload = payload.replace("\"null\"", "null").replace(
        "\"false\"", "false").replace("\"true\"", "true")
    return payload


def add_min_price(df):
    price_cols = [col for col in df.columns if 'price' in col]
    df['min_price'] = df[price_cols].min(skipna=True, axis=1)
    return df


def get_routes(origin="Aurillac", destination="Brive la Gaillarde", date_trip=datetime.now().isoformat()):
    data = get_data(origin, destination, date_trip)
    response = requests.request("POST", URL, data=data, headers=headers)

    time.sleep(5)

    response_dict = response.json()

    result_list = response_dict['results']

    print "\n Itineraries found for {0}-{1}: {2}\n".format(origin, destination, len(result_list))
    df = concat_results(result_list)
    df = add_min_price(df)
    return df


def convert_result_to_dataframe(result):

    df = pd.DataFrame()

    df = pd.DataFrame.from_records(result['segments'])
    if result['pushProposalType'] == 'BUS':
        print "BUUUUUUUUUS"
        return

    if result['unsellableReason'] == "FULL_TRAIN":
        print "FULL TRAIN"
        return

    df[['departureDate', 'arrivalDate']] = df[['departureDate', 'arrivalDate']
                                              ].applymap(lambda x: pd.to_datetime(x, format="%Y-%m-%dT%H:%M:%S"))
    df['total_duration'] = df['arrivalDate'].iloc[-1] - \
        df['departureDate'].iloc[0]
    df['trip_name'] = u' to '.join([result['origin'], result['destination']])
    df['trip_id'] = result['id']
    df['unsellableReason'] = result['unsellableReason']
    df['TGV'] = 'TGV' in df['transporter'].values
    df['total_trains'] = df.shape[0]
    df['trip_rank'] = df.index
    df['trip_departureDate'] = result['departureDate']
    df['trip_arrivalDate'] = result['arrivalDate']

    for price_key in result['priceProposals'].keys():
        df[''.join(["price_", price_key])] = result[
            'priceProposals'][price_key]['amount']

    return df


def concat_results(json_result):
    df = pd.DataFrame()

    for result in json_result:

        try:
            df_result = convert_result_to_dataframe(result)

            df = pd.concat([df, df_result], axis=0)
        except Exception as e:
            print "error for {}\n \n".format(result)
            print "error rootacause : \n \n", e.args
    return df
