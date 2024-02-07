import smtplib
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os

github_action = 'https://github.com/plana-planetarium/pixiv_sync/actions'

mail_host = 'smtp.qq.com'
mail_user = os.getenv('EMAIL_USERNAME').replace('@qq.com', '')
mail_pass = os.getenv('EMAIL_PASSWORD')

sender = os.getenv('EMAIL_USERNAME')

text = '[%s] 自动添加用户至同步程序 successfully\n\n' % (github_action.replace('https://github.com/', '').replace('/actions', '').replace('/actions/', ''))
subject = '[%s] 自动添加用户至同步程序 successfully' % (github_action.replace('https://github.com/', '').replace('/actions', '').replace('/actions/', ''))

def message_config():
    content = MIMEText(text)
    message = MIMEMultipart()
    message.attach(content)
    message['From'] = 'Pixiv Sync Notice' + '<'+ sender + '>'
    message['To']   = 'Admin'
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
