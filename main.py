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
import config_parser

from PyQt5 import QtWidgets


def init_threads_list(requests_session, config, window):
    kucoin_update_thread = multithreads.KuCoinPairUpdaterThread
    tradeogre_update_thread = multithreads.TradeOgrePairUpdaterThread
    update_helper_thread = multithreads.UpdateHelper
    conf = config.config_dict
    print(conf['window'])

    threads_list = [[conf['pairs']['box1']['exchange'], conf['pairs']['box1']['pair_code1']['code'], '0', conf['window']['update_time']],
                    [conf['pairs']['box1']['exchange'], conf['pairs']['box1']['pair_code2']['code'], '1', conf['window']['update_time']],
                    [conf['pairs']['box2']['exchange'], conf['pairs']['box2']['pair_code1']['code'], '2', conf['window']['update_time']],
                    [conf['pairs']['box2']['exchange'], conf['pairs']['box2']['pair_code2']['code'], '3', conf['window']['update_time']]]

    threads = []
    for thread in threads_list:
        print(thread[0])
        this_thread = None
        if thread[0] == 'KuCoin':
            this_thread = kucoin_update_thread(requests_session,
                                 thread[1],
                                 conf['api']['kucoin']['keys'],
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

    config = config_parser.Config('settings.json')
    config.parse_config()
    requests_session = requests.session()

    app = QtWidgets.QApplication(sys.argv)
    main_window = gui.MainApp()
    main_window.show()

    pairs = [
        ['KuCoin', 'TRTL-BTC', '0', 10],
        ['KuCoin', 'TRTL-ETH', '1', 10],
        ['TradeOgre', 'LTC-TRTL', '2', 10],
        ['TradeOgre', 'BTC-TRTL', '3', 10]
    ]
    init_threads_list(requests_session, config, main_window)
    app.exec_()

if __name__ == '__main__':
    main()
