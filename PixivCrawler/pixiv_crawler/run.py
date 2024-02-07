from config import DOWNLOAD_CONFIG
from crawlers.users_crawler import UserCrawler
from utils import checkDir
import os


if __name__ == "__main__":

    checkDir(DOWNLOAD_CONFIG["STORE_PATH"])

    app = UserCrawler(artist_id=os.getenv('USER_ID'), capacity=2048)
    app.run()
