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
        gui_dict = self.gui_model_dict
        pair_dict = self.kucoin_pair.pair_pool

        update_dict = ['time', 'price', 'volume', 'high', 'low']
        for name in update_dict:
            gui_dict[name].setText(pair_dict[name])
        gui_dict['pair_name'].setText('🔗' + pair_dict['pair_codes_vars']['converted'])

        for table_name in ['sell', 'buy']:
            pair_table = pair_dict['orders'][table_name]
            gui_table = gui_dict[table_name]

            if pair_table:
                gui_table.setRowCount(len(pair_table))
                gui_table.setColumnCount(2)
                for i, row in enumerate(pair_table):
                    to_insert = [list(pair_table.keys())[i],
                                 pair_table[row]]
                    for a, col in enumerate(to_insert):
                        gui_table.setItem(i, a, QTableWidgetItem(col))
            else:
                # ¯\_(ツ)_/¯
                gui_table.setRowCount(1)
                gui_table.setColumnCount(1)
                gui_table.setItem(0, 0, QTableWidgetItem('¯\\_(ツ)_/¯'))


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
        self._parser = api_parser.TradeOgreGrabber(self.pair_code, self.session, self.api)

    def update_pair_model(self):
        self.tradeogre_pair.parse_info(self._parser.grab())

    def update_gui(self):
        gui_dict = self.gui_model_dict
        pair_dict = self.tradeogre_pair.pair_pool

        update_dict = ['time', 'price', 'volume', 'high', 'low']
        for name in update_dict:
            gui_dict[name].setText(pair_dict[name])

        gui_dict['pair_name'].setText('🔗' + pair_dict['pair_codes_vars']['converted'])

        for table_name in ['sell', 'buy']:
            pair_table = pair_dict['orders'][table_name]
            gui_table = gui_dict[table_name]

            if pair_table:
                gui_table.setRowCount(len(pair_table))
                gui_table.setColumnCount(2)
                # ¯\_(ツ)_/¯
                for i, row in enumerate(pair_table):
                    to_insert = [list(pair_table.keys())[i],
                                 pair_table[row]]
                    for a, col in enumerate(to_insert):
                        gui_table.setItem(i, a, QTableWidgetItem(col))
            else:
                gui_table.setRowCount(1)
                gui_table.setColumnCount(1)
                gui_table.setItem(0, 0, QTableWidgetItem('¯\\_(ツ)_/¯'))

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
