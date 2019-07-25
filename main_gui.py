import design

from PyQt5 import QtWidgets


class MainApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
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

        self.pairs_elements = {
            '0': {
                'time': self.update_time1,
                'pair_name': self.pair_name1,
                'price': self.price1, 'price_converted': self.price_converted1,
                'volume': self.volume1, 'volume_converted': self.volume_converted1,
                'high': self.high1, 'high_converted': self.high_converted1,
                'low': self.low1, 'low_converted': self.low_converted1,
                'buy': self.buy_table1, 'sell': self.sell_table1
            },
            '1': {
                'time': self.update_time2,
                'pair_name': self.pair_name2,
                'price': self.price2, 'price_converted': self.price_converted2,
                'volume': self.volume2, 'volume_converted': self.volume_converted2,
                'high': self.high2, 'high_converted': self.high_converted2,
                'low': self.low2, 'low_converted': self.low_converted2,
                'buy': self.buy_table2, 'sell': self.sell_table2
            },
            '2': {
                'time': self.update_time3,
                'pair_name': self.pair_name3,
                'price': self.price3, 'price_converted': self.price_converted3,
                'volume': self.volume3, 'volume_converted': self.volume_converted3,
                'high': self.high3, 'high_converted': self.high_converted3,
                'low': self.low3, 'low_converted': self.low_converted3,
                'buy': self.buy_table3, 'sell': self.sell_table3
            },
            '3': {
                'time': self.update_time4,
                'pair_name': self.pair_name4,
                'price': self.price4, 'price_converted': self.price_converted4,
                'volume': self.volume4, 'volume_converted': self.volume_converted4,
                'high': self.high4, 'high_converted': self.high_converted4,
                'low': self.low4, 'low_converted': self.low_converted4,
                'buy': self.buy_table4, 'sell': self.sell_table4
            }
        }
