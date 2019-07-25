import requests
import time

import api_models


class KucoinGrabber:
    def __init__(self, pair, requests_session, auth, api):
        self.auth = auth
        self.pair = pair
        self.session = requests_session
        self.api = api

    def grab(self):
        info_dict = {
            'time': time.strftime("%d.%m %H:%M:%S", time.localtime()),
            '24h_info': self.api.client.get_24hr_stats(self.pair),
            'orders': self.api.client.get_order_book(self.pair)
            }
        return info_dict

class TradeOgreGrabber:
    def __init__(self, pair, requests_session, api):
        self.pair = pair
        self.session = requests_session
        self.api = api

    def grab(self):
        info_dict = {
            'time': time.strftime("%d.%m %H:%M:%S", time.localtime()),
            '24h_info': self.api.get_market_currency(self.pair),
            'orders': self.api.get_order_book(self.pair)
            }
        return info_dict
