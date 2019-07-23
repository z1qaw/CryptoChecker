import sys
from PyQt5 import QtWidgets
import design

class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.allert_symbol1.hide()
        self.allert_symbol2.hide()
        self.allert_symbol3.hide()
        self.allert_symbol4.hide()
        self.price_converted1.hide()
        self.volume_converted1.hide()
        self.high_converted1.hide()
        self.low_converted1.hide()
        self.price_converted2.hide()
        self.volume_converted2.hide()
        self.high_converted2.hide()
        self.low_converted2.hide()
        self.price_converted3.hide()
        self.volume_converted3.hide()
        self.high_converted3.hide()
        self.low_converted3.hide()
        self.price_converted4.hide()
        self.volume_converted4.hide()
        self.high_converted4.hide()
        self.low_converted4.hide()

        self.pairs_elements = {
            '0': {
                'update_time': self.update_time1,
                'pair_name': self.pair_name1,
                'price': self.price1, 'price_converted': self.price_converted1,
                'volume': self.volume1, 'volume_converted': self.volume_converted1,
                'high': self.high1, 'high_converted': self.high_converted1,
                'low': self.low1, 'low_converted': self.low_converted1,
                'buy_table': self.buy_table1, 'sell_table': self.sell_table1
                 },
            '1': {
                'update_time': self.update_time2,
                'pair_name': self.pair_name2,
                'price': self.price2, 'price_converted': self.price_converted2,
                'volume': self.volume2, 'volume_converted': self.volume_converted2,
                'high': self.high2, 'high_converted': self.high_converted2,
                'low': self.low2, 'low_converted': self.low_converted2,
                'buy_table': self.buy_table2, 'sell_table': self.sell_table2
                 },
            '2': {
                'update_time': self.update_time3,
                'pair_name': self.pair_name3,
                'price': self.price3, 'price_converted': self.price_converted3,
                'volume': self.volume3, 'volume_converted': self.volume_converted3,
                'high': self.high3, 'high_converted': self.high_converted3,
                'low': self.low3, 'low_converted': self.low_converted3,
                'buy_table': self.buy_table3, 'sell_table': self.sell_table3
                 },
            '3': {
                'update_time': self.update_time4,
                'pair_name': self.pair_name4,
                'price': self.price4, 'price_converted': self.price_converted4,
                'volume': self.volume4, 'volume_converted': self.volume_converted4,
                'high': self.high4, 'high_converted': self.high_converted4,
                'low': self.low4, 'low_converted': self.low_converted4,
                'buy_table': self.buy_table4, 'sell_table': self.sell_table4
                 }
        }
