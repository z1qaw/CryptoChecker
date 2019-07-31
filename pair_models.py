import re


class PairModel:
    def __init__(self, pair_name):
        self.pair_pool = {
            'time': None,
            'pair_name': pair_name,
            'pair_codes_vars': {
                'original': None,
                'converted': None
            },
            'pair_reversed': False,
            'price': None,
            'to_btc': None,
            'to_btc_price': None,
            'volume': None,
            'high': None,
            'low': None,
            'pair_uri': None,
            'orders': {
                'buy': {},
                'sell': {}
            }
        }

    def convert_pair_code(self, pair_code):
        main = ['BTC', 'ETH', 'KCS', 'USD', 'NEO', 'LTC']
        if re.findall('\w+-\w', pair_code):
            found_codes = re.findall('\w+', pair_code)
            self.pair_pool['pair_codes_vars']['original'] = pair_code
            if len(found_codes) == 2:
                if (found_codes[0] in main) and (found_codes[1] not in main):
                    found_codes.reverse()
                    self.pair_pool['pair_reversed'] = True
                self.pair_pool['pair_codes_vars']['converted'] = '/'.join(found_codes)
        else:
            self.pair_pool['pair_codes_vars'] = None

    def parse_info(self, info_dict):
        if self.pair_pool['pair_name'] == 'KuCoin':
            self.pair_pool['time'] = info_dict['time']
            self.convert_pair_code(info_dict['24h_info']['symbol'])
            self.pair_pool['price'] = info_dict['24h_info']['last']
            self.pair_pool['volume'] = info_dict['24h_info']['volValue']
            self.pair_pool['high'] = info_dict['24h_info']['high']
            self.pair_pool['low'] = info_dict['24h_info']['low']

            self.pair_pool['to_btc'] = True if info_dict['to_btc'] else False
            self.pair_pool['to_btc_price'] = info_dict['converted'] if self.pair_pool['to_btc'] else None

            if info_dict['orders']:

                for ask in info_dict['orders']['asks']:
                    if self.pair_pool['pair_reversed']:
                        self.pair_pool['orders']['buy'][ask[1]] = ask[0]
                    else:
                        self.pair_pool['orders']['buy'][ask[0]] = ask[1]

                for bid in info_dict['orders']['bids']:
                    if self.pair_pool['pair_reversed']:
                        self.pair_pool['orders']['sell'][bid[1]] = bid[0]
                    else:
                        self.pair_pool['orders']['sell'][bid[0]] = bid[1]

        if self.pair_pool['pair_name'] == 'TradeOgre':
            self.pair_pool['time'] = info_dict['time']
            pair_name = list(info_dict['24h_info'].keys())[0]
            self.convert_pair_code(pair_name)
            self.pair_pool['price'] = info_dict['24h_info'][pair_name]['price']
            self.pair_pool['volume'] = info_dict['24h_info'][pair_name]['volume']
            self.pair_pool['high'] = info_dict['24h_info'][pair_name]['high']
            self.pair_pool['low'] = info_dict['24h_info'][pair_name]['low']

            self.pair_pool['to_btc'] = True if info_dict['to_btc'] else False
            self.pair_pool['to_btc_price'] = info_dict['converted'] if self.pair_pool['to_btc'] else None

            if info_dict['orders']:
                self.pair_pool['orders']['buy'] = info_dict['orders']['sell']
                self.pair_pool['orders']['sell'] = (info_dict['orders']['buy'])
