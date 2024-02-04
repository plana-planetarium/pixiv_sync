from send_email import email_tool
import os

file = os.getenv('NAME_USER') + '.txt'

with open('./sync_require/' + file, 'r') as file_open:
    text = file_open.read()
file_open.close()

text = text.split('\n')

if_file = os.listdir('./Downloads/' + file.replace('.txt', ''))
if if_file == []:
    upload_name = '!!!NO FILE NEED TO UPLOAD!!!'
else:
    upload_name = text[-2]

i = 1

email_url = ''
while i <= len(text)-5:
    email_url += text[i] + '\n'
    i += 1

email_tool(receiver = text[0], URL = email_url, upload_name = upload_name, status_num = text[-3], name = text[-2], user_update = text[-1])
