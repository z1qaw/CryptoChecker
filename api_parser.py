import re
import time
from decimal import Decimal
from mpmath import mpf, nstr


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
            'orders': self.api.client.get_order_book(self.pair),
            'to_btc': False,
            'converted': None
        }
        if not re.findall('BTC', self.pair):
            curr = re.findall('\w+', self.pair)
            btc_price = self.api.client.get_24hr_stats(curr[1] + '-BTC')['last']
            converted = nstr(mpf(info_dict['24h_info']['last']) * mpf(btc_price), 50)[:13]
            info_dict['to_btc'] = True
            info_dict['converted'] = converted

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
            'orders': self.api.get_order_book(self.pair),
            'to_btc': False,
            'converted': None
        }

        if not re.findall('BTC', self.pair):
            curr = re.findall('\w+', self.pair)
            btc_curr = 'BTC-' + curr[0]
            btc_price = self.api.get_market_currency(btc_curr)[btc_curr]['price']
            converted = nstr(mpf(info_dict['24h_info'][self.pair]['price']) * mpf(btc_price), 50)[:13]
            info_dict['to_btc'] = True
            info_dict['converted'] = converted

        return info_dict
