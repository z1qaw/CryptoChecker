import requests
from kucoin.client import Client


class TradeOgreApi:
    def __init__(self, requests_session):
        self.api_uri = 'https://tradeogre.com/api/v1'
        self.session = requests_session


    def get_markets(self):
        '''Return Markets in JSON format.'''
        this_uri = self.api_uri + '/markets'
        answer = requests.get(this_uri)
        return answer.json()

    def get_market_currency(self, market_name):
        markets = self.get_markets()
        found_market = None

        for x, market in enumerate(markets):
            if list(market.keys())[0] == market_name:
                found_market = markets[x]
                break

        return found_market

    def get_mk_cur_by_list(self, markets_list):
        markets = self.get_markets()
        found_markets = []

        for x, market in enumerate(markets):
            if list(market.keys())[0] in markets_list:
                found_markets.append(markets[x])

        return found_markets

    def get_order_book(self, market_name):
        this_uri = self.api_uri + '/orders/' + market_name
        answer = requests.get(this_uri)
        return answer.json()

class KucoinApi:
    def __init__(self, requests_session, auth):
        self.api_uri = 'https://openapi-sandbox.kucoin.com'
        self.api_key = auth['api_key']
        self.api_secret = auth['api_secret']
        self.api_passphrase = auth['api_passphrase']
        self.client = Client(self.api_key, self.api_secret, self.api_passphrase)

    def get_markets(self):
        markets = self.client.get_markets()
        return markets
