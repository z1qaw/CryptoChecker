import settings_design

from PyQt5 import QtWidgets


class SettingsApp(QtWidgets.QMainWindow, settings_design.Ui_Form):
    def __init__(self, config):
        super().__init__()
        self.setupUi(self)

        config_dict = config.config_dict

        table_settings = {
            'pin': {
                'name': 'Pin window on top', 'type': 'boolean', 'option': config_dict['window']['pin']
            }, 'toolbar': {
                'name': 'Show toolbar', 'type': 'boolean', 'option': config_dict['window']['toolbar']
            }, 'window_title': {
                'name': 'Show window title', 'type': 'boolean', 'option': config_dict['window']['window_title']
            }, 'dark': {
                'name': 'Dark theme', 'type': 'boolean', 'option': config_dict['window']['dark']
            }, 'orders': {
                'name': 'Show pair orders', 'type': 'boolean', 'option': config_dict['window']['orders']
            }, 'opacity': {
                'name': 'Window opacity', 'type': 'int', 'from': 0, 'to': 100, 'option': config_dict['window']['opacity']
            }, 'autoupdate': {
                'name': 'Pairs autoupdate', 'type': 'boolean', 'option': config_dict['pairs']['autoupdate']
            }, 'update_time': {
                'name': 'Update time', 'type': 'int', 'from': 5, 'to': 86400, 'option': config_dict['pairs']['update_time']
            }, 'box1_exchange': {
                'name': 'Box 1 exchange', 'type': 'list', 'items': ['KuCoin', 'TradeOgre'], 'option': config_dict['pairs']['box1']['exchange']
            }, 'box2_exchange': {
                'name': 'Box 2 exchange', 'type': 'list', 'items': ['KuCoin', 'TradeOgre'], 'option': config_dict['pairs']['box2']['exchange']
            }, 'pair_1_currency': {
                'name': 'Pair 1 currency', 'type': 'string', 'option': config_dict['pairs']['box1']['pair_code1']
            }, 'pair_2_currency': {
                'name': 'Pair 2 currency', 'type': 'string', 'option': config_dict['pairs']['box1']['pair_code2']
            }, 'pair_3_currency': {
                'name': 'Pair 3 currency', 'type': 'string', 'option': config_dict['pairs']['box2']['pair_code1']
            }, 'pair_4_currency': {
                'name': 'Pair 4 currency', 'type': 'string', 'option': config_dict['pairs']['box2']['pair_code2']
            }, 'kucoin_api_key': {
                'name': 'KuCoin API key', 'type': 'password', 'option': config_dict['api']['kucoin']['keys']['api_key']
            }, 'kucoin_api_secret': {
                'name': 'KuCoin API secret', 'type': 'password', 'option': config_dict['api']['kucoin']['keys']['api_secret']
            }, 'kucoin_api_passphrase': {
                'name': 'KuCoin API passphrase', 'type': 'password', 'option': config_dict['api']['kucoin']['keys']['api_passphrase']
            }, 'activate_proxy': {
                'name': 'Use proxy', 'type': 'boolean', 'option': config_dict['proxy']['active']
            }, 'proxy_type': {
                'name': 'Proxy type', 'type': 'list', 'items': ['HTTP', 'SOCKS5'], 'option': config_dict['proxy']['type']
            }, 'proxy_host': {
                'name': 'Proxy host', 'type': 'string', 'option': config_dict['proxy']['host']
            }, 'proxy_port': {
                'name': 'Use proxy', 'type': 'string', 'option': config_dict['proxy']['port']
            },
        }

        self.config_table.setColumnCount(2)
        self.config_table.setRowCount(len(table_settings))

        for num, option in enumerate(table_settings):
            if table_settings[option]['type'] == 'boolean':
                combo = QtWidgets.QComboBox(self)
                self.config_table.setItem(num, 0, QtWidgets.QTableWidgetItem(table_settings[option]['name']))
                self.config_table.setCellWidget(num, 1, combo)
                print(option)