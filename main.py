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
from datetime import datetime, timedelta

base_url = "https://api.polygon.io"


def consume_api():
    ticker_code = "AAPL"
    start_date = '2020-01-01'
    end_date = '2020-12-31'
    timespan = "month"
    multiplier = "1"

    url = f"{base_url}/v2/aggs/ticker/{ticker_code}/range/{multiplier}/{timespan}/{start_date}/{end_date}"
    api_response_results = do_api_request(url).get("results")

    stock_results = []
    for result in api_response_results:
        entry_price = result.get("c")
        raw_date = datetime(1970, 1, 1) + timedelta(milliseconds=result.get("t"))
        entry_date = raw_date.strftime("%d-%m-%Y")
        stock_results.append({"date": entry_date, "close_price": entry_price})

    return stock_results


def do_api_request(url):
    return requests.get(url, params={"apiKey": "VIHLKoUL4Adg3jVwYXSnUu3phXlsM74U"}).json()


def parse_to_csv(results: list):
    csv_file = open("stock_timeseries.csv", "w")

    writer = csv.writer(csv_file)

    header = results[0].keys()
    writer.writerow(list(header))

    for entry in results:
        writer.writerow([entry.get("date"), entry.get("close_price")])

    csv_file.close()


stock_history = consume_api()

parse_to_csv(stock_history)
