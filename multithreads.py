import threading
import os
import time

from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem

import api_models
import pair_models
import api_parser


class UpdateHelper():
    def __init__(self, threads_list, threads_paused, pause_time):
        self.threads_list = threads_list
        self.threads_paused = threads_paused
        self.pause_time = pause_time

    def start_threads(self):
        for thread in self.threads_list:
            thread.start()

    def pause_thread(self):
        for thread in self.threads_list:
            thread.set_paused()

    def set_pause_time(self, pause_time):
        for thread in self.threads_list:
            thread.pause_time = pause_time


class KuCoinPairUpdaterThread(threading.Thread):
    def __init__(self, requests_session, pair_code, kucoin_auth_dict, gui_model_dict, pause_time):
        super(KuCoinPairUpdaterThread, self).__init__()
        self.setDaemon(True)
        self.pause_time = 10
        self.paused = False
        self.model_name = 'KuCoin'
        self.session = requests_session
        self.pair_code = pair_code
        self.kucoin_auth_dict = kucoin_auth_dict
        self.gui_model_dict = gui_model_dict

        self.api = api_models.KucoinApi(self.session, self.kucoin_auth_dict)
        self.kucoin_pair = pair_models.PairModel(self.model_name)
        self._parser = api_parser.KucoinGrabber(self.pair_code, self.session, self.kucoin_auth_dict, self.api)


    def update_pair_model(self):
        self.kucoin_pair.parse_info(self._parser.grab())

    def update_gui(self):
        self.gui_model_dict['update_time'].setText(self.kucoin_pair.pair_pool['time'])
        self.gui_model_dict['pair_name'].setText(self.kucoin_pair.pair_pool['pair_codes_vars']['converted'])
        self.gui_model_dict['price'].setText(self.kucoin_pair.pair_pool['price'])
        self.gui_model_dict['volume'].setText(self.kucoin_pair.pair_pool['volume'])
        self.gui_model_dict['high'].setText(self.kucoin_pair.pair_pool['high'])
        self.gui_model_dict['low'].setText(self.kucoin_pair.pair_pool['low'])

        self.gui_model_dict['buy_table'].setRowCount(len(self.kucoin_pair.pair_pool['orders']['buy']))
        self.gui_model_dict['buy_table'].setColumnCount(2)

        for i, row in enumerate(self.kucoin_pair.pair_pool['orders']['buy']):
            to_insert = [list(self.kucoin_pair.pair_pool['orders']['buy'].keys())[i],
                         self.kucoin_pair.pair_pool['orders']['buy'][row]]
            for a, col in enumerate(to_insert):
                self.gui_model_dict['buy_table'].setItem(i, a, QTableWidgetItem(col))

        self.gui_model_dict['sell_table'].setRowCount(len(self.kucoin_pair.pair_pool['orders']['sell']))
        self.gui_model_dict['sell_table'].setColumnCount(2)

        for i, row in enumerate(self.kucoin_pair.pair_pool['orders']['sell']):
            to_insert = [list(self.kucoin_pair.pair_pool['orders']['sell'].keys())[i],
                         self.kucoin_pair.pair_pool['orders']['sell'][row]]
            for a, col in enumerate(to_insert):
                self.gui_model_dict['sell_table'].setItem(i, a, QTableWidgetItem(col))

    def set_paused(self):
        self.paused = True

    def set_resumed(self):
        self.paused = False

    def set_pause_time(self, pause_time):
        self.pause_time(pause_time)

    def run(self):
        while True:
            if not self.paused:
                self.update_pair_model()
                self.update_gui()
            time.sleep(self.pause_time)


class TradeOgrePairUpdaterThread(threading.Thread):
    def __init__(self, requests_session, pair_code, gui_model_dict, pause_time):
        super(TradeOgrePairUpdaterThread, self).__init__()
        self.setDaemon(True)

        self.paused = False
        self.model_name = 'TradeOgre'
        self.session = requests_session
        self.pair_code = pair_code
        self.gui_model_dict = gui_model_dict
        self.pause_time = 10

        self.api = api_models.TradeOgreApi(self.session)
        self.tradeogre_pair = pair_models.PairModel(self.model_name)
        self._parser = api_parser.TradeOgreGrabber(self.pair_code,  self.session, self.api)

    def update_pair_model(self):
        self.tradeogre_pair.parse_info(self._parser.grab())

    def update_gui(self):
        self.gui_model_dict['buy_table'].setRowCount(0)
        self.gui_model_dict['sell_table'].setRowCount(0)
        self.gui_model_dict['buy_table'].setColumnCount(2)
        self.gui_model_dict['sell_table'].setColumnCount(2)

        self.gui_model_dict['update_time'].setText(self.tradeogre_pair.pair_pool['time'])
        self.gui_model_dict['pair_name'].setText(self.tradeogre_pair.pair_pool['pair_codes_vars']['converted'])
        self.gui_model_dict['price'].setText(self.tradeogre_pair.pair_pool['price'])
        self.gui_model_dict['volume'].setText(self.tradeogre_pair.pair_pool['volume'])
        self.gui_model_dict['high'].setText(self.tradeogre_pair.pair_pool['high'])
        self.gui_model_dict['low'].setText(self.tradeogre_pair.pair_pool['low'])

        if self.tradeogre_pair.pair_pool['orders']['buy']:
            self.gui_model_dict['buy_table'].setRowCount(len(self.tradeogre_pair.pair_pool['orders']['buy']))
            self.gui_model_dict['buy_table'].setColumnCount(2)
            # ¯\_(ツ)_/¯
            for i, row in enumerate(self.tradeogre_pair.pair_pool['orders']['buy']):
                to_insert = [list(self.tradeogre_pair.pair_pool['orders']['buy'].keys())[i],
                             self.tradeogre_pair.pair_pool['orders']['buy'][row]]
                for a, col in enumerate(to_insert):
                    self.gui_model_dict['buy_table'].setItem(i, a, QTableWidgetItem(col))
        else:
            self.gui_model_dict['buy_table'].setRowCount(1)
            self.gui_model_dict['buy_table'].setColumnCount(1)
            self.gui_model_dict['buy_table'].setItem(0, 0, QTableWidgetItem('¯\\_(ツ)_/¯'))


        if self.tradeogre_pair.pair_pool['orders']['sell']:

            self.gui_model_dict['sell_table'].setRowCount(len(self.tradeogre_pair.pair_pool['orders']['sell']))
            self.gui_model_dict['sell_table'].setColumnCount(2)

            for i, row in enumerate(self.tradeogre_pair.pair_pool['orders']['sell']):
                to_insert = [list(self.tradeogre_pair.pair_pool['orders']['sell'].keys())[i],
                             self.tradeogre_pair.pair_pool['orders']['sell'][row]]
                for a, col in enumerate(to_insert):
                    self.gui_model_dict['sell_table'].setItem(i, a, QTableWidgetItem(col))
        else:
            self.gui_model_dict['sell_table'].setRowCount(1)
            self.gui_model_dict['sell_table'].setColumnCount(1)
            self.gui_model_dict['sell_table'].setItem(0, 0, QTableWidgetItem('¯\\_(ツ)_/¯'))

    def run(self):
        while True:
            if not self.paused:
                self.update_pair_model()
                self.update_gui()
            time.sleep(self.pause_time)
