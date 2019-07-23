import sys
import requests
import os

import api_models
import pair_models
import api_parser
import design
import gui
import multithreads
import _settings

from PyQt5 import QtWidgets


def init_threads_list(requests_session, window, threads_list):
    kucoin_update_thread = multithreads.KuCoinPairUpdaterThread
    tradeogre_update_thread = multithreads.TradeOgrePairUpdaterThread
    update_helper_thread = multithreads.UpdateHelper

    threads = []

    for thread in threads_list:
        this_thread = None
        if thread[0] == 'KuCoin':
            this_thread = kucoin_update_thread(requests_session,
                                 thread[1],
                                 _settings.KuCoinApiDict,
                                 window.pairs_elements[thread[2]],
                                 thread[3]
                                 )
        if thread[0] == 'TradeOgre':
            this_thread = tradeogre_update_thread(requests_session,
                                    thread[1],
                                    window.pairs_elements[thread[2]],
                                    thread[3]
                                    )
        threads.append(this_thread)

    helper = update_helper_thread(threads, False, 10)
    helper.start_threads()



def main():
    try:
        requests_session = requests.session()
        app = QtWidgets.QApplication(sys.argv)
        main_window = gui.MainApp()
        main_window.show()

        if os.path.ex
        pairs = [
            ['KuCoin', 'TRTL-BTC', '0', 10],
            ['KuCoin', 'TRTL-ETH', '1', 10],
            ['TradeOgre', 'LTC-TRTL', '2', 10],
            ['TradeOgre', 'BTC-TRTL', '3', 10]
        ]
        init_threads_list(requests_session, main_window, pairs)
        app.exec_()
    except Exception as e:
        print(e.message)

if __name__ == '__main__':
    main()
