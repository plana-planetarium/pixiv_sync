import os
import datetime
from send_email import email_tool

os.environ['SET_TIME'] = str(datetime.date.today() - datetime.timedelta(days=1)).replace('-', '/')

require_files = os.listdir('./sync_require')
for file in require_files:
    with open('./sync_require/' + file, 'r') as file_open:
        text = file_open.read()
    file_open.close()
    text = text.split('\n')
    i = 0
    name = text[i].replace('## ', '')
    i += 1
    email_adress = text[i].replace('#', '').replace(' ', '')
    i += 1
    url = []
    url_email = ''
    while i <= len(text)-1:
        if text[i] != '':
            url += [text[i]]
            url_email += text[i] + ', '
        i += 2
    #NOTE name --> 需求中填写的昵称
    #     email_adress --> 邮箱地址
    #     url --> type: list 更新地址列表
    #     url_email --> 纯文本地址集，仅用添加至正文

    email_tool(receiver = email_adress, URL = url_email[:-2], upload_name = name, status_num = '1', name = name, user_update = '')

    os.environ['USER_NAME'] = '../../Downloads/' + name + '/'
    os.chdir('./PixivCrawler/pixiv_crawler/')
    #NOTE https://www.pixiv.net/users/16034374
    for url_download in url:
        url_id = url_download.replace('https://www.pixiv.net/users/', '')
        os.environ['USER_ID'] = url_id

        os.system('python run.py')

    os.chdir('../../Downloads/' + name)

    down_user = os.listdir('./')
    #NOTE 现在所处目录:Downloads/name/
    #     user_update --> list 包含所更新画师的PIC

    down_user = os.listdir('./')
    user_update = down_user
    
    user_update = str(user_update).replace('[', '').replace(']', '').replace("'", '')

    if user_update == '':
        url_email = '!!!NO USER NEED TO UPDATE!!!..'
        user_update = '!!!NO USER NEED TO UPDATE!!!'
        name = '!!!NO USER NEED TO UPDATE!!!'

    email_tool(receiver = email_adress, URL = url_email[:-2], upload_name = name, status_num = '2', name = name, user_update = user_update)

    os.chdir('../..')

    with open('./sync_require/' + file, 'w') as file_open:
        file_open.write(email_adress + '\n' + url_email[:-2] + '\n' + name + '\n' + '3' + '\n' + name + '\n' + user_update)
    file_open.close()
