import os
import json


class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config_dict = None
        self.default_config_dict = {
            'window': {
                'log_to_console': True,
                'log_to_file': False,
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
                        'api_key': '',
                        'api_secret': '',
                        'api_passphrase': ''
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
                file.write(json.dumps(self.default_config_dict, sort_keys=True, indent=4))

    def parse_config(self):
        with open(self.filename, 'r') as file:
            self.config_dict = json.loads(file.read())

    def save_to_file(self):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(self.config_dict, sort_keys=True, indent=4))
