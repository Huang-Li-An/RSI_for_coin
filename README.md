RSI_for_coin!

參數：
	-coin:要做RSI的貨幣
	-period:每幾個小時取一次資料
	-base:每幾筆資料做一次RSI
	-sender:寄件者
	-passwd:寄件者密碼
	-receiver:收件者
	-mode:1or2 (1:執行，2:觀看圖)


功能：
	利用電腦的排程:crontab，每小時執行一次程式。
	每次抓取最新的data算一次RSI
	當RSI < 20 or RSI > 80 or 黃金交叉點 or 死亡交叉點時，寄信通知！

用法：
	Ubuntu環境：
		terminal-> crontab -e，編輯此檔案(都使用絕對路徑)
		輸入：
		SHELL=/bin/sh
		PATH=/bin:/sbin:/usr/bin:/sur/sbin:/usr/local/bin:/usr/local/sbin:~/bin
		PYTHONPATH=$PYTHONPATH:/home/lian/.local/lib/python3.5/site-packages/
		1 * * * * python3 main.py(絕對路徑) -coin eth -period 2 -base 12 -sender xxx@gmail.com -passwd xxx -receiver yyy@gmail.com -mode 1 > xxx.log(絕對路徑) 2>&1

		此設定能控制每小時執行，並且把output記錄下來


*********
1.第一次使用時，必須先到Huobi.py的__init__，將os.chdir()，指定到main.py的資料夾
2.crontab必須要設定python的環境變數，否則會找不到一些library
  方法:到terminal執行python3
  	  import xxx
  	  xxx.__file__  (可以得到該library的路徑，假設是/home/doubt_even/.local/lib/python2.7/site-packages/)
  接著到crontab的文件裡添加：PYTHONPATH=$PYTHONPATH:/home/doubt_even/.local/lib/python2.7/site-packages/
