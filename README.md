# 一个简单的自动更新pixiv画师作品下载器

## 原理

爬虫部分基于 [PixivCrawler](https://github.com/CWHer/PixivCrawler.git) 修改实现

部署在Github Actions，每日早上6点开始同步昨日更新作品，且会有邮件更进

## 使用方法

### fork该项目于自己的仓库

### 爬虫基础设置

#### 添加actions变量(secrets)

- PIXIV_ID: 你的pixiv帐号

- PIXIV_COOKIE: 你的pixiv COOKIE,获取方法见PixivCrawler的README中"COOKIE"项的设置

#### 邮件推送设置

##### 添加actions变量(secrets)

- EMAIL_USERNAME: 邮箱小号(用于推送)

- EMAIL_PASSWORD: 邮箱小号SMTP授权码

- 注：默认使用的是QQ邮箱，如须更改邮箱SMTP服务器请修改`send_email.py`中`mail_host = 'smtp.qq.com'`和`mail_user = os.getenv('EMAIL_USERNAME').replace('@qq.com', '')`

##### 修改`send_email.py`

- 修改`github_action = 'https://github.com/plana-planetarium/pixiv_sync/actions'` 中的链接为你自己的github actions链接

##### 修改`change_email.py`

- 修改`github_action = 'https://github.com/plana-planetarium/pixiv_sync/actions'` 中的链接为你自己的github actions链接

- 修改`smtpObj.sendmail(sender, '3412294524@qq.com', message.as_string())`中的邮箱地址为你的邮箱地址

#### 下载链接配置

- 删除`sync_require`文件夹下所有文件(这些文件是我的链接配置)

- 新建一个txt文本文档，标题为你的昵称(注意满足文件及文件夹命名规范)，后缀为txt

- 按照以下格式写入信息(注意#和空格)


```
## name (你的昵称，和文本文档昵称保持一致)
# email adress (你的邮箱地址，用于邮件推送)
https://www.pixiv.net/users/xxxxxxxxx (所需同步的画师网页地址)
    -->unknow (备注信息，可以乱填，但是必须要填写，没有固定格式，仅需保证有本行且本行不为空白)
https://www.pixiv.net/users/xxxxxxxxx (所需同步的画师网页地址)
    -->unknow (备注信息，可以乱填，但是必须要填写，没有固定格式，仅需保证有本行且本行不为空白)
```

- 注: 每次添加新的文本文档需要修改`add.change`文件，任意修改，仅需保证文件内容被修改即可，用于生成新的Github Actions运行文件，若仅是修改需同步的链接，则无需修改

#### 提交到你自己的仓库

- 提交后注意查看Actions是否又有一个Update项目(自动添加用户)运行，并注意运行状态，或等待邮件推送

#### 等待每日推送

- 更新完后的下载文件在Github Actions中获取
