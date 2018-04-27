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
		到etc/crontab，編輯此檔案
		輸入：* */1 * * * root python3 main.py的路徑 -coin eth -period 2 -base 12 -sender xxx@gmail.com -passwd xxx -receiver yyy@gmail.com -mode 1


*********
第一次使用時，必須先到Huobi.py的__init__，將os.chdir()，指定到main.py的資料夾


