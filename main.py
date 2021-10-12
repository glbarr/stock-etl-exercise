# This will be a python routine to get the historical monthly quote of certain tickers and organizer them in a csv file
# We are going to use the Poligon.io APIS for this
# useful links: https://polygon.io/docs/get_v1_open-close__stocksTicker___date__anchor
"""""
 For this let's try to use a top down approach to solve the problem
 
 After reading the docs I have concluded that the api to be used is the Aggregate (Bars) api, it gives me a lot of 
 information on the given symbol, from that information I'll be looking to get only the closing price for the month 
 and the timestamp (That is in Unix Msec). 
 
"""""

import csv
import requests
import datetime

base_url = "https://api.polygon.io"


def consume_api():

    ticker_code = "AAPL"
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    timespan = "month"
    multiplier = "1"
    ts_result = {'date':[], 'close_price': []}
    api_response = do_api_request(f"{base_url}/v2/aggs/ticker/{ticker_code}/range/{multiplier}/{timespan}/{start_date}/{end_date}")

    for i in api_response.get('results'):
        for key, value in i.items():
            if key == 't':
                ts_result['date'].append(i.get(key))
            elif key == 'c':
                ts_result['close_price'].append(i.get(key))
    return ts_result


def do_api_request(url):

    return requests.get(url, params={"apiKey": "VIHLKoUL4Adg3jVwYXSnUu3phXlsM74U"}).json()


def parse_to_csv(results: dict):
    csv_file = open("stock_timeseries.csv", "w")

    writer = csv.writer(csv_file)
    writer.writerow(['Date', 'Close Price'])
    price_history = {}

    for key, value in results.items():
        if key == 'date':
            a = 5

    csv_file.close()


stock_history = consume_api()

parse_to_csv(stock_history)
