import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

mail_host = 'smtp.qq.com'
mail_user = os.getenv('EMAIL_USERNAME').replace('@qq.com', '')
mail_pass = os.getenv('EMAIL_PASSWORD')

sender = os.getenv('EMAIL_USERNAME')

text = '[plana-planetarium/pixiv_sync] 自动添加用户至同步程序 successfully\n\n'
subject = '[plana-planetarium/pixiv_sync] 自动添加用户至同步程序 successfully'

def message_config():
    content = MIMEText(text)
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = 'A.R.O.N.A' + '<'+ sender + '>'
    message['To']   = 'A.R.O.N.A'
    message['Subject'] = Header(subject, 'utf-8')

    return message
    

def send_mail(message):
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, '3412294524@qq.com', message.as_string())
    except Exception as e:
        print(e)

message = message_config()
send_mail(message)
print("Sent email successfully")
