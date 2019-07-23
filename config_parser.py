import re
import os
import json

class Config:
    def __init__(self, filename):
        self.filename = filename

        self.default_config_dict = {
            'window': {
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
                    'encrypted_keys': '',
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
                file.write(str(self.default_config_dict))

    def parse_config(self):
        with open(self.filename, 'r') as file:
            self.config_dict = json.loads(file.read())

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            self.config_dict = json.loads(file.read())
