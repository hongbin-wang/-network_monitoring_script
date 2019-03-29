import os
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header


ip="10.8.30.195"

def main():
    while True:
        ping=os.system("ping -c 4 -w 4 %s"%ip)
        if ping:
            return True
def mail():
    mail_host=("")  #设置服务器
    mail_user=" "    #用户名
    mail_pass=""   #口令
    sender = ''
    receivers = ['']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    #message['From'] = Header("wangcq", 'utf-8')
    subject = '脚本自动'
    message = MIMEText("脚本自动:%s   ,   %s,ping不通！"%(ti,ip) ,'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        #在阿里云运行脚本，默认25端口被封闭，可以申请解除。这里使用的ssl
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mail_host, XX)    #  XX，SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        with open(r"log.txt","a+",encoding="utf-8") as f:
            f.write("邮件发送成功")
        #print ("邮件发送成功")
    except smtplib.SMTPException:
        with open(r"log.txt","a+",encoding="utf-8") as f:
            f.write("Error: 无法发送邮件")
        #print ("Error: 无法发送邮件")
if __name__ == '__main__':
        ti=time.strftime("%Y-%m-%d-%H:%M", time.localtime())
        if main():
            mail()
