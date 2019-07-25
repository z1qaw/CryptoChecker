import sys
import requests

import main_gui
import multithreads
import config_parser

from PyQt5 import QtWidgets

import settings_gui


def init_threads_list(requests_session, config, window):
    kucoin_update_thread = multithreads.KuCoinPairUpdaterThread
    tradeogre_update_thread = multithreads.TradeOgrePairUpdaterThread
    update_helper_thread = multithreads.UpdateHelper
    conf = config.config_dict

    threads_list = [[conf['pairs']['box1']['exchange'], conf['pairs']['box1']['pair_code1']['code'], '0',
                     conf['window']['update_time']],
                    [conf['pairs']['box1']['exchange'], conf['pairs']['box1']['pair_code2']['code'], '1',
                     conf['window']['update_time']],
                    [conf['pairs']['box2']['exchange'], conf['pairs']['box2']['pair_code1']['code'], '2',
                     conf['window']['update_time']],
                    [conf['pairs']['box2']['exchange'], conf['pairs']['box2']['pair_code2']['code'], '3',
                     conf['window']['update_time']]]

    threads = []
    for thread in threads_list:
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

    helper = update_helper_thread(threads, False, conf['window']['update_time'])
    helper.start_threads()


def main():
    ui_elements = []

    config = config_parser.Config('settings.json')
    config.parse_config()
    requests_session = requests.session()
    settings_dict = config.config_dict

    if settings_dict['proxy']['active']:
        requests_session.proxies = {
            'http': '{0}://{1}:{2}'.format(
                    settings_dict['proxy']['type'],
                    settings_dict['proxy']['host'],
                    settings_dict['proxy']['port']
            )
        }

    app = QtWidgets.QApplication(sys.argv)
    main_window = main_gui.MainApp()

    settings_window = settings_gui.SettingsApp()
    ui_elements.append(settings_window)

    main_window.show()

    init_threads_list(requests_session, config, main_window)
    app.exec_()


if __name__ == '__main__':
    main()
