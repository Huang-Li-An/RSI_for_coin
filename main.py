from Huobi import *
import sys


if __name__ == '__main__':
    for i in range(1, len(sys.argv), 2):
        if ( sys.argv[i] == '-coin'):
            s_coin = sys.argv[i+1]
        if ( sys.argv[i] == '-period'):
            i_period = int(sys.argv[i+1])
        if ( sys.argv[i] == '-base'):
            i_base = int(sys.argv[i+1])
        if ( sys.argv[i] == '-sender'):
            s_sender = sys.argv[i+1]
        if ( sys.argv[i] == '-passwd'):
            s_passwd = sys.argv[i+1]
        if ( sys.argv[i] == '-receiver'):
            s_receiver = sys.argv[i+1]
        if ( sys.argv[i] == '-mode'):
            i_mode = int(sys.argv[i + 1])


    coin = Huobi(s_coin, i_period, i_base, s_sender, s_passwd, s_receiver)
    coin.start(i_mode)


