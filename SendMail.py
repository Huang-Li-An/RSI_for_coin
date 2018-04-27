import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SendMail:
    def __init__(self, s_sender, s_passwd, s_receiver, s_filename ):
        self.s_sender = s_sender
        self.s_passwd = s_passwd
        self.s_receiver = s_receiver
        self.s_filename = s_filename + '.png'

    def send(self, s_content ):
        # 创建一个带附件的实例
        msg = MIMEMultipart()
        msg['From'] = self.s_sender
        msg['To'] = self.s_receiver
        msg['Subject'] = Header( '準備投資了！！！', 'utf-8')

        # 邮件正文内容
        msg.attach(MIMEText(s_content, 'plain', 'utf-8'))

        # 构造附件1（附件为TXT格式的文本）
        '''
        att1 = MIMEText(open('text1.txt', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="text1.txt"'
        msg.attach(att1)

        # 构造附件3（附件为HTML格式的网页）  
        att3 = MIMEText(open('report_test.html', 'rb').read(), 'base64', 'utf-8')  
        att3["Content-Type"] = 'application/octet-stream'  
        att3["Content-Disposition"] = 'attachment; filename="report_test.html"' 
        '''
        # 构造附件2（附件为JPG格式的图片）
        att2 = MIMEText(open( self.s_filename, 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="' + self.s_filename + '"'
        msg.attach(att2)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login( self.s_sender, self.s_passwd )
        server.send_message(msg)
        server.quit()

        print('Email sent!')
