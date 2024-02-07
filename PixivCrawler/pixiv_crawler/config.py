import datetime
import os

OUTPUT_CONFIG = {
    # verbose / simplified output
    "VERBOSE": False,
    "PRINT_ERROR": False
}

NETWORK_CONFIG = {
    # proxy setting
    #   you should customize your proxy setting accordingly
    #   default is for clash
    #"PROXY": {"https": "127.0.0.1:20171"},

    # common request header
    "HEADER": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
    }
}

USER_CONFIG = {
    # user id
    #   access your pixiv user profile to find this
    #   e.g. https://www.pixiv.net/users/xxxx
    "USER_ID": os.getenv("PIXIV_ID"),
    "COOKIE": os.getenv("PIXIV_COOKIE")
}


DOWNLOAD_CONFIG = {
    # set time which day need to download
    #"SET_TIME": "2020/02/12",
    "SET_TIME": os.getenv("SET_TIME"),

    # image save path
    #   NOTE: DO NOT miss "/"
    #"STORE_PATH": "../../Downloads/$USER_NAME/",
    "STORE_PATH": os.getenv("USER_NAME"),

    # abort request / download
    #   after 10 unsuccessful attempts
    "N_TIMES": 10,

    # waiting time (s) after failure
    "FAIL_DELAY": 1,

    # max parallel thread number
    "N_THREAD": 32,
    # waiting time (s) after thread start
    "THREAD_DELAY": 1,
}
