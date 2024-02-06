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
#receiver = os.getenv('EMAIL_RECEIVER')
#receiver 
#input_id = os.getenv('EMAIL_ID')
#URL = os.getenv('URL')

#upload_name = os.getenv('USER')
#status_num = os.getenv('STATUS')

def email_tool(receiver, URL, upload_name, status_num, name, user_update):

    status_workflow = ['Prepared', 'Downloaded', 'Compressed & Uploaded']
    text_detials = \
            'Here are some details: \n' + \
            '    Download URL: %s\n' % str(URL) + \
            '    Upload package name: %s.zip\n' % str(upload_name) + \
            'To get more details, you can visit the following website: https://github.com/plana-planetarium/pixiv_sync/actions'
    
    
    #if input_id != '':
    #        receiver =  receiver + ', ' + input_id
    #
    receivers = receiver.replace(' ','').split(',')
    
    def get_text(status, next_status):
        text = \
                '[plana-planetarium/pixiv_sync] 自动同步pixiv上的画师文件 (%s/3) %s successfully\n\n' % (str(status_num), str(status)) + \
                'This part of workflow has been succeed. This part is about %s.\n' % str(status).replace('ed', 'ing').lower() + \
                '%s\n' % str(next_status) + \
                text_detials
        return text
    
    def get_subject(status):
        subject = '[plana-planetarium/pixiv_sync] (%s/3) %s successfully' % (str(status_num), str(status))
        return subject
    
    if int(status_num) <= 2:
        status = str(status_workflow[int(status_num) - 1])
        next_status = \
                'The next part is about %s. The next part will be started now.\n' % str(status_workflow[int(status_num)]).replace('ed', 'ing').lower() + \
                'Please wait for a moment.\n'
        text = get_text(status, next_status)
        subject = get_subject(status)
    else:
        text_detials = \
                'Here are some details: \n' + \
                '    Download URL: %s\n' % str(URL) + \
                '    Updated PIC: %s\n' % str(user_update) + \
                '    Upload package name: %s.zip\n' % str(upload_name) + \
                'To get more details, you can visit the following website: https://github.com/plana-planetarium/pixiv_sync/actions'
        status = str(status_workflow[int(status_num) - 1])
        next_status = 'This part is the last part of workflow. So that you can download your artifact on Github Actions.\n'
        text = get_text(status, next_status)
        subject = get_subject(status)
    
    
    def message_config():
        content = MIMEText(text)
        message = MIMEMultipart()
        message.attach(content)
        message['From'] = 'A.R.O.N.A' + '<'+ sender + '>'
        message['To']   = name
        message['Subject'] = Header(subject, 'utf-8')
    
        return message
        
    
    def send_mail(message):
        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
        except Exception as e:
            print(e)
    
    message = message_config()
    send_mail(message)
    print("Sent email successfully")
