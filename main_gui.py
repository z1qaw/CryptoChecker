import os
import webbrowser

import main_design

from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore


def open_settings_in_editor():
    from sys import platform
    if platform == "linux" or platform == "linux2":
        osCommandString = 'gedit settings.json'
        os.system(osCommandString)
    elif platform == "win32":
        osCommandString = 'notepad.exe settings.json'
        os.system(osCommandString)


class MainApp(QtWidgets.QMainWindow, main_design.Ui_MainWindow):
    def __init__(self, settings_dict, pairs_dict):
        super().__init__()
        self.setupUi(self)

        to_hide = [
            self.allert_symbol1, self.allert_symbol2, self.allert_symbol3,
            self.allert_symbol3, self.allert_symbol4, self.price_converted1,
            self.volume_converted1, self.high_converted1, self.low_converted1,
            self.price_converted2, self.volume_converted2, self.high_converted2,
            self.low_converted2, self.price_converted3, self.volume_converted3,
            self.high_converted3, self.low_converted3, self.price_converted4,
            self.volume_converted4, self.high_converted4, self.low_converted4
        ]

        for el in to_hide:
            el.hide()

        orders = [
            self.orders1, self.orders2, self.orders3, self.orders4
        ]

        self.toolbar_widget.setVisible(False)

        if not settings_dict['window']['orders']:
            for el in orders:
                el.setVisible(False)

        if settings_dict['window']['transparent']:
            self.setAttribute(Qt.WA_TranslucentBackground, True)

        if settings_dict['window']['pin']:
            self.setWindowFlags(QtCore.Qt.Window | Qt.WindowStaysOnTopHint)

        self.resize(self.minimumSize())
        self.setWindowOpacity(settings_dict['window']['opacity'])

        self.pair_group1.setTitle(settings_dict['pairs']['box1']['exchange'] + ':')
        self.pair_group2.setTitle(settings_dict['pairs']['box2']['exchange'] + ':')

        self.pairs_elements = {
            '0': {
                'time': self.update_time1,
                'pair_name': self.pair_name1,
                'browser_button': self.browser_button1,
                'price': self.price1, 'price_converted': self.price_converted1,
                'volume': self.volume1, 'volume_converted': self.volume_converted1,
                'high': self.high1, 'high_converted': self.high_converted1,
                'low': self.low1, 'low_converted': self.low_converted1,
                'buy': self.buy_table1, 'sell': self.sell_table1
            },
            '1': {
                'time': self.update_time2,
                'pair_name': self.pair_name2,
                'browser_button': self.browser_button2,
                'price': self.price2, 'price_converted': self.price_converted2,
                'volume': self.volume2, 'volume_converted': self.volume_converted2,
                'high': self.high2, 'high_converted': self.high_converted2,
                'low': self.low2, 'low_converted': self.low_converted2,
                'buy': self.buy_table2, 'sell': self.sell_table2
            },
            '2': {
                'time': self.update_time3,
                'pair_name': self.pair_name3,
                'browser_button': self.browser_button3,
                'price': self.price3, 'price_converted': self.price_converted3,
                'volume': self.volume3, 'volume_converted': self.volume_converted3,
                'high': self.high3, 'high_converted': self.high_converted3,
                'low': self.low3, 'low_converted': self.low_converted3,
                'buy': self.buy_table3, 'sell': self.sell_table3
            },
            '3': {
                'time': self.update_time4,
                'pair_name': self.pair_name4,
                'browser_button': self.browser_button4,
                'price': self.price4, 'price_converted': self.price_converted4,
                'volume': self.volume4, 'volume_converted': self.volume_converted4,
                'high': self.high4, 'high_converted': self.high_converted4,
                'low': self.low4, 'low_converted': self.low_converted4,
                'buy': self.buy_table4, 'sell': self.sell_table4
            }
        }

        self.link1 = None
        self.link2 = None
        self.link3 = None
        self.link4 = None

        if pairs_dict[0]['exchange'] == 'KuCoin':
            self.link1 = 'https://www.kucoin.com/trade/' + pairs_dict[0]['pair']
        elif pairs_dict[0]['exchange'] == 'TradeOgre':
            self.link1 = 'https://tradeogre.com/exchange/' + pairs_dict[0]['pair']
        else:
            self.pairs_elements[str(0)]['browser_button'].setDisabled(True)

        if pairs_dict[1]['exchange'] == 'KuCoin':
            self.link2 = 'https://www.kucoin.com/trade/' + pairs_dict[1]['pair']
        elif pairs_dict[1]['exchange'] == 'TradeOgre':
            self.link2 = 'https://tradeogre.com/exchange/' + pairs_dict[1]['pair']
        else:
            self.pairs_elements[str(1)]['browser_button'].setDisabled(True)

        if pairs_dict[2]['exchange'] == 'KuCoin':
            self.link3 = 'https://www.kucoin.com/trade/' + pairs_dict[2]['pair']
        elif pairs_dict[2]['exchange'] == 'TradeOgre':
            self.link3 = 'https://tradeogre.com/exchange/' + pairs_dict[2]['pair']
        else:
            self.pairs_elements[str(2)]['browser_button'].setDisabled(True)

        if pairs_dict[3]['exchange'] == 'KuCoin':
            self.link4 = 'https://www.kucoin.com/trade/' + pairs_dict[3]['pair']
        elif pairs_dict[3]['exchange'] == 'TradeOgre':
            self.link4 = 'https://tradeogre.com/exchange/' + pairs_dict[3]['pair']
        else:
            self.pairs_elements[str(3)]['browser_button'].setDisabled(True)

        self.browser_button1.clicked.connect(self.link1_pressed)
        self.browser_button2.clicked.connect(self.link2_pressed)
        self.browser_button3.clicked.connect(self.link3_pressed)
        self.browser_button4.clicked.connect(self.link4_pressed)

        self.actionOpen_settings_in_editor.triggered.connect(open_settings_in_editor)
        self.actionReload_app.triggered.connect(self.reload_app)

    def link1_pressed(self):
        webbrowser.open_new_tab(self.link1)

    def link2_pressed(self):
        webbrowser.open_new_tab(self.link2)

    def link3_pressed(self):
        webbrowser.open_new_tab(self.link3)

    def link4_pressed(self):
        webbrowser.open_new_tab(self.link4)

    def reload_app(self):
        self.close()
