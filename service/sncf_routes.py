# coding: utf-8

import json
import pandas as pd
import requests
#import ipdb


from config import URL, headers


def get_data(origin, destination, date):

    null = 'null'
    false = 'false'
    true = 'true'
    destination = "Brive-la-Gaillarde"
    destinationCode = "FRBVE"

    payload = {"origin": "Aurillac", "originCode": "FRAUR", "originLocation": null, "destination": "Clermont-Ferrand", "destinationCode": destinationCode, "destinationLocation": null, "directTravel": false, "asymmetrical": false, "professional": false, "customerAccount": false, "oneWayTravel": true, "departureDate": "2017-08-21T13:00:00", "returnDate": null, "travelClass": "SECOND", "country": "FR", "language": "fr", "busBestPriceOperator": null, "busOnly": false, "passengers": [
        {"travelerId": null, "profile": "ADULT", "age": 26, "birthDate": null, "fidelityCardType": "NONE", "fidelityCardNumber": null, "commercialCardNumber": null, "commercialCardType": "NONE", "promoCode": "", "lastName": null, "firstName": null, "phoneNumer": null, "hanInformation": null}], "animals": [], "bike": "NONE", "withRecliningSeat": false, "physicalSpace": null, "fares": [], "withBestPrices": false, "highlightedTravel": null, "nextOrPrevious": false, "source": "FORM_SUBMIT", "targetPrice": null, "han": false, "$initial": true, "$queryId": "SRlEN"}

    payload = json.dumps(payload)
    payload = payload.replace("\"null\"", "null").replace(
        "\"false\"", "false").replace("\"true\"", "true")
    return payload


def get_routes(origin, destination, date):
    data = get_data(origin, destination, date)
    response = requests.request("POST", URL, data=data, headers=headers)

    response_dict = response.json()
    result_dict = response_dict['results']

    df = concat_results(result_dict)
    return df


def convert_result_to_dataframe(result):

    df = pd.DataFrame()

    df = pd.DataFrame.from_records(result['segments'])

    df[['departureDate', 'arrivalDate']] = df[['departureDate', 'arrivalDate']
                                              ].applymap(lambda x: pd.to_datetime(x, format="%Y-%m-%dT%H:%M:%S"))
    df['total_duration'] = df['arrivalDate'].iloc[-1] - \
        df['departureDate'].iloc[0]
    df['trip_name'] = u' to '.join([result['origin'], result['destination']])
    df['trip_id'] = result['id']
    df['unsellableReason'] = result['unsellableReason']
    df['TGV'] = 'TGV' in df['transporter'].values
    df['total_trains'] = df.shape[0]

    for price_key in result['priceProposals'].keys():
        df[''.join(["priresult_dictce_", price_key])] = result[
            'priceProposals'][price_key]['amount']

    return df


def concat_results(json_result):
    df = pd.DataFrame()
    print "Results FOUND : {}\n".format(len(json_result))
    for result in json_result:

        try:
            df_result = convert_result_to_dataframe(result)
            df = pd.concat([df, df_result], axis=0)
        except Exception as e:
            print "error for {}".format(result)
            print e.args
    return df
