import requests
import json
import matplotlib.pyplot as plt
import time
import os
from SendMail import *

class Huobi:

    def __init__(self, s_coin, i_period, i_base, s_sender, s_passwd, s_receiver ):
        self.s_url = 'https://api.huobi.pro/market/history/kline?symbol={}&period=60min&size={}'
        self.l_data = []
        self.l_rsi = []

        self.s_pname = ''  # for email attachment name
        self.s_content = ''
        self.s_sender = s_sender
        self.s_passwd = s_passwd
        self.s_receiver = s_receiver

        self.s_coin = s_coin + 'usdt'
        self.i_period = i_period
        self.i_base = i_base
        self.i_num =  (i_base*2+1+10)*i_period  # 固定算出可以算10個rsi的量，總共需要這麼多小時的資料量
        #print(os.getcwd())
        os.chdir('/home/lian/桌面/RSI_for_coin')

    def getData(self):
        html = requests.get( self.s_url.format( self.s_coin, str(self.i_num) ) ).text
        d = json.loads(html)['data']

        # 得到開盤的值
        for i in d:
            self.l_data.append( str(i['open']) )


        print('New data: ' + str(self.l_data[0]))


    def writeData(self):
        path = './' + self.s_coin + '/' + self.s_coin + '_data.txt'

        f = open( path, 'w' )
        for i in range(0, len(self.l_data), self.i_period):
            f.write( self.l_data[i] + '\n')
        f.close()

    '''
    def writeNewData(self, coin ):
        #寫入新資料到txt的第一行,並刪除最後一行
        path = './' + coin + '/' + coin + '_data.txt'
        f = open(path,'r')
        l = f.readlines()
        l.insert(0, str(self.data[0]) + '\n')
        f.close()

        f = open(path, 'w')
        for i in l[:-1]:
            f.write(i)
        f.close()
    '''

    def calculateRSI(self, i_base):
        path = './' + self.s_coin + '/' + self.s_coin + '_data.txt'

        self.l_data = []
        f = open( path, 'r' )
        self.l_data = f.readlines()

        self.l_data = list( map(lambda x: float(x), self.l_data ) )
        self.l_rsi = []

        for i in range(10):
            f_raise = 0.0  # 紀錄漲的數量
            l_gap = []   # 每一個間距的漲幅
            k = i
            for j in range(i_base):
                f_tmp = self.l_data[k] - self.l_data[k+1]
                k += 1
                if ( f_tmp > 0.0 ):
                    f_raise += f_tmp
                else:
                    f_tmp *= -1.0

                l_gap.append( f_tmp )

            self.l_rsi.append( (f_raise/sum(l_gap))/self.i_period*100 )


        print( 'New RSI_' + str(i_base) + ': ' + str(self.l_rsi[0]) )


    def writeRSI(self, i_base):
        path = './' + self.s_coin + '/' + self.s_coin + '_RSI_' + str(i_base) + '.txt'
        f = open(path, 'w')
        for i in self.l_rsi:
            f.write(str(i) + '\n')
        f.close()

    '''
    def writeNewRSI(self, coin, base):
        path = './' + coin + '/' + coin + '_RSI_' + str(base) + '.txt'
        self.rsi.append(100)
        f = open(path, 'r')
        l = f.readlines()
        l.insert(0, str(self.rsi[0]) +'\n')
        f.close()

        f = open(path, 'w')
        for i in l[:-1]:
            f.write(i)
        f.close()
    '''

    def drawPicture(self, mode):
        path = './' + self.s_coin + '/' + self.s_coin + '_RSI_' + str(self.i_base) +'.txt'
        f = open(path, 'r' )
        l_s = f.readlines()
        l_s = list( map( lambda x:float(x), l_s ) )

        self.s_content = self.s_coin + '-> RSI_' + str(self.i_base) + '\n' + '\t' + str(l_s) + '\n'
        #print('RSI_' + str(self.i_base))
        #print('\t' + str(l_s))
        l_s.reverse()
        f.close()

        path = './' + self.s_coin + '/' + self.s_coin + '_RSI_' + str(self.i_base*2) + '.txt'
        f = open(path, 'r')
        l_l = f.readlines()
        l_l = list(map(lambda x: float(x), l_l))

        self.s_content += self.s_coin + '-> RSI_'+ str(self.i_base*2) + '\n' + '\t' + str(l_l) + '\n'
        #print('RSI_'+str(self.i_base*2))
        #print('\t' + str(l_l))
        l_l.reverse()
        f.close()

        l_tmp = [ i for i in range(0, self.i_period*10, self.i_period) ]
        group_labels = [ i for i in range(0, self.i_period*10, self.i_period) ]
        group_labels.reverse()

        plt.plot( l_tmp, l_s )
        plt.plot( l_tmp, l_l )
        plt.xticks( l_tmp, group_labels)
        plt.legend([ str(self.i_base*self.i_period) + 'hours', str(self.i_base*2*self.i_period)+ 'hours'])
        plt.xlabel( 'Hours ago' )
        plt.ylabel( 'RSI number' )
        plt.title( self.s_coin)
        if ( mode == 1 ):
            t = time.localtime(time.time())
            self.s_pname = self.s_coin + '_' + str(t[0]) + '_' + str(t[1]) + '_' + str(t[2]) + '_' + str(t[3]) + '_' + str(t[4])
            plt.savefig(self.s_pname)
        elif ( mode == 2 ):
            print( self.s_content )
            plt.show()


    def checkTiming(self):
        path = './' + self.s_coin + '/' + self.s_coin + '_RSI_' + str(self.i_base) + '.txt'
        f = open(path, 'r')
        l_s = f.readlines()
        l_s = list(map(lambda x: float(x), l_s))
        f.close()

        path = './' + self.s_coin + '/' + self.s_coin + '_RSI_' + str(self.i_base * 2) + '.txt'
        f = open(path, 'r')
        l_l = f.readlines()
        l_l = list(map(lambda x: float(x), l_l))
        f.close()

        f_sNow = l_s[0]
        f_sPre = l_s[1]
        f_lNow = l_l[0]


        if ( f_sNow > f_sPre):
            if ( f_sNow > f_lNow > f_sPre ):
                self.drawPicture(1)
                user = SendMail(self.s_sender, self.s_passwd, self.s_receiver, self.s_pname)
                user.send('黃金交叉，快買啊！！！\n'+ self.s_content)
        if (f_sPre > f_sNow):
            if ( f_sPre > f_lNow > f_sNow ):
                self.drawPicture(1)
                user = SendMail(self.s_sender, self.s_passwd, self.s_receiver, self.s_pname)
                user.send('死亡交叉，快賣啊！！！\n'+ self.s_content)

        if ( f_sNow > 80.0 ):
            self.drawPicture(1)
            user = SendMail(self.s_sender, self.s_passwd, self.s_receiver, self.s_pname)
            user.send('RSI大於80了，準備要賣囉！！！\n' + self.s_content)

        if ( f_sNow < 20.0 ):
            self.drawPicture(1)
            user = SendMail(self.s_sender, self.s_passwd, self.s_receiver, self.s_pname)
            user.send('RSI小於20了，準備要買囉！！！\n' + self.s_content)



    def start(self, mode ):
        if ( mode == 1 ):
            # excute in every period
            self.getData()
            self.writeData()

            self.calculateRSI(self.i_base)
            self.writeRSI(self.i_base)

            self.calculateRSI(self.i_base*2)
            self.writeRSI(self.i_base*2)
            self.checkTiming()

        elif ( mode == 2 ):
            # to see RSI picture
            self.drawPicture(2)
            #self.checkTiming()