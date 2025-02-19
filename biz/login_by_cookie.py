import logging
import os
import time
import json
from time import sleep
import globals


def delay_start(seconds):
    while seconds > 0:
        minutes_remaining = seconds // 60
        seconds_remaining = seconds % 60
        logging.info("程序将在 " + str(minutes_remaining) + "分钟 " + str(seconds_remaining) + " 秒后开始启动!")
        time.sleep(1)
        seconds -= 1


def check_cookie_valid():
    folder_path = './cookie'
    file_name = globals.my_user_id + '.txt'
    for i in range(globals.max_checks):
        if os.path.exists(os.path.join(folder_path, file_name)):
            logging.info('登录成功！')
            return True
        else:
            logging.warn('未登录，或者Cookie失效，请重新登录, waiting...')
            time.sleep(1)
    return False;


def login_by_cookie(bro, cookie_path):
    """
    根据保存的Cookie信息进行登录
    :param bro:
    :param cookie_path:
    :return:
    """
    try:
        with open(cookie_path, 'r', encoding='utf-8') as f:
            cookies = f.readlines()
        for cookie in cookies:
            cookie = cookie.replace(r'\n', '')
            cookie_li = json.loads(cookie)
            sleep(1)
            for cookie in cookie_li:
                bro.add_cookie(cookie)
            bro.refresh()
        print('使用cookie自动登录成功！')
        sleep(1)
    except Exception as e:
        print(e)
        print('登录失败')


# if __name__ == '__main__':
#     # 初始化
#     bro, chains = init_webdriver()
#     bro.get(globals.home_url)
#     # 登录
#     cookie_path = '../cookie/' + globals.my_user_id + '.txt'
#     login_by_cookie(bro, cookie_path)
#     input()
#     bro.quit()