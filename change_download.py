def change_program(url_id, name):
    example_run = \
            'from config import DOWNLOAD_CONFIG\n' + \
            'from crawlers.users_crawler import UserCrawler\n' + \
            'from utils import checkDir\n' + \
            'import os\n' + \
            'if __name__ == "__main__":\n' + \
            '    checkDir(DOWNLOAD_CONFIG["STORE_PATH"])\n' + \
            '    app = UserCrawler(artist_id=%s, capacity=10240)\n' % url_id + \
            '    app.run()'

    example_config = \
            'import datetime\n' + \
            'import os\n' + \
            'OUTPUT_CONFIG = {\n' + \
            '    "VERBOSE": False,\n' + \
            '    "PRINT_ERROR": False\n' + \
            '}\n' + \
            'NETWORK_CONFIG = {\n' + \
            '    "HEADER": {\n' + \
            '        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",\n' + \
            '    }\n' + \
            '}\n' + \
            'USER_CONFIG = {\n' + \
            '    "USER_ID": os.getenv("PIXIV_ID"),\n' + \
            '    "COOKIE": os.getenv("PIXIV_COOKIE")\n' + \
            '}\n' + \
            'DOWNLOAD_CONFIG = {\n' + \
            '    "STORE_PATH": "../../Downloads/%s/",\n' %name + \
            '    "N_TIMES": 10,\n' + \
            '    "WITH_TAG": False,\n' + \
            '    "FAIL_DELAY": 1,\n' + \
            '    "N_THREAD": 32,\n' + \
            '    "THREAD_DELAY": 1,\n' + \
            '}'
    with open('./PixivCrawler/config.py', 'w') as config_write:
        config_write.write(example_config)
    config_write.close()
    
    with open('./PixivCrawler/run.py', 'w') as config_run:
        config_run.write(example_run)
    config_run.close()

#NOTE config need "url_id"
#     run need "name"
#     remember to change user_id and cook, get from env
