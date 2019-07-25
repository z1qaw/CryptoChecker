import re
import os
import json


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config_dict = None
        self.default_config_dict = {
            'window': {
                'autoupdate': False,
                'update_time': 10,
                'pin': False,
                'toolbar': True,
                'dark': False,
                'opacity': 100
            },
            'pairs': {
                'box1': {
                    'exchange': 'KuCoin',
                    'pair_code1': {'code': 'TRTL-BTC', 'exists': True},
                    'pair_code2': {'code': 'TRTL-ETH', 'exists': True}
                },
                'box2': {
                    'exchange': 'TradeOgre',
                    'pair_code1': {'code': 'LTC-TRTL', 'exists': True},
                    'pair_code2': {'code': 'BTC-TRTL', 'exists': True}
                }
            },
            'api': {
                'kucoin': {
                    'keys': {
                        'api_key': '5d2bba3e134ab759f6130eee',
                        'api_secret': 'b572e0a1-6c19-4c87-afe6-ce41d4e3a468',
                        'api_passphrase': 'FFFFFFFDSFDSFD'
                    },
                    'valid': False
                }
            },
            'proxy': {
                'active': False,
                'type': None,
                'host': None,
                'port': None
            }
        }

        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as file:
                file.write(str(self.default_config_dict).replace('\'', '\"').replace('False', 'false').replace('True', 'true').replace('None', 'null'))

    def parse_config(self):
        with open(self.filename, 'r') as file:
            self.config_dict = json.loads(file.read())

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            file.write(str(self.config_dict))
