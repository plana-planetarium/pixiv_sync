import os
import datetime
from send_email import email_tool
from change_download import change_program

os.system('mkdir ./Downloads')

require_files = os.listdir('./sync_require')
for file in require_files:
    with open('./sync_require/' + file, 'r') as file_open:
        text = file_open.read()
    file_open.close()
    text = text.split('\n')
    i = 0
    name = text[i].replace('#', '').replace(' ', '')
    i += 1
    email_adress = text[i].replace('#', '').replace(' ', '')
    i += 1
    url = []
    url_email = ''
    while i <= len(text)-1:
        if text[i] != '':
            url += [text[i]]
            url_email += text[i] + '\n'
        i += 2
    #NOTE name --> 需求中填写的昵称
    #     email_adress --> 邮箱地址
    #     url --> type: list 更新地址列表
    #     url_email --> 纯文本地址集，仅用添加至正文

    with open('./downloads_log/' + file, 'r') as file_open:
        text = file_open.read()
    file_open.close()
    down_log = text.split(',')
    #NOTE down_log --> 以跟新过的图片文件名


    email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '1', name = name, user_update = '')

    os.system('''mkdir "./Downloads/''' + name + '''"''')
    os.chdir('./Downloads/' + name)

    for file_log in down_log:
        if file_log != '':
            os.system('echo " " > ' + file_log)

    


    #NOTE https://www.pixiv.net/users/16034374
    for url_download in url:
        url_id = url_download.replace('https://www.pixiv.net/users/', '')
        os.chdir('../..')
        change_program(url_id, name)

        os.chdir('./PixivCrawler/pixiv_crawler')
        os.system('python run.py')

    #email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '2', name = name, user_update = '')

    os.chdir('../../Downloads/' + name)

    down_user = os.listdir('./')
    #user_update = os.listdir('./') 

    all_file = str(down_user).replace('[', '').replace(']', '').replace("'", '')

    down_user_list = [i for i in down_user if i not in down_log]
    down_user = down_user_list
    user_update = down_user_list
        
    #NOTE 现在所处目录:Downloads/name/
    #     user_update --> list 包含所更新画师的PIC

    for rm_file in down_log:
        if rm_file != '':
            os.system('rm ' + rm_file)
    
    user_update = str(user_update).replace('[', '').replace(']', '').replace("'", '')

    if user_update == '':
        url_email = '!!!NO USER NEED TO UPDATE!!!\n'
        user_update = '!!!NO USER NEED TO UPDATE!!!'
        name = '!!!NO USER NEED TO UPDATE!!!'

    email_tool(receiver = email_adress, URL = url_email, upload_name = name, status_num = '2', name = name, user_update = user_update)

    os.chdir('../..')

    with open('./sync_require/' + file, 'w') as file_open:
        file_open.write(email_adress + '\n' + url_email[:-1] + '\n' + name + '\n' + '3' + '\n' + name + '\n' + user_update)
    file_open.close()

    with open('./downloads_log/' + file, 'w') as file_open:
        file_open.write(all_file)
    file_open.close()
