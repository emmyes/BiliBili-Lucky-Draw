import json
import logging
from datetime import datetime
from time import sleep
from urllib.parse import urlparse
from selenium.webdriver.common.by import By

from biz.login_by_cookie import delay_start
from globals import home_url, delay_time
from utils.selenium_util import init_webdriver, init_webdriver_for_gen_cookie
from utils.xpath_util import is_xpath_exist
logging.basicConfig(level=logging.INFO)

def login_manual(bro):
    while is_xpath_exist(bro, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/li/div') is True:
        print(datetime.now().strftime("%H:%M:%S") + '：等待扫描登录')
        sleep(1)
    print('登录成功，正在保存cookie')
    dict_cookies = bro.get_cookies()
    json_cookies = json.dumps(dict_cookies)
    sleep(3)
    try:
        url = bro.find_element(By.XPATH, '//*[@id="i_cecream"]/div[2]/div[1]/div[1]/ul[2]/li[1]/div[1]/a[1]').get_attribute("href")
    except Exception as e:
        print(e)
    result = urlparse(url)
    id = str(result[2])[1:]
    cookie_path = './cookie/' + id + '.txt'
    with open(cookie_path, 'w') as f:
        f.write(json_cookies)
    print('cookies保存成功！')


if __name__ == '__main__':
    delay_start(int(delay_time))
    # 初始化
    bro, chains = init_webdriver_for_gen_cookie()
    bro.get(home_url)
    # 登录
    login_manual(bro)
    bro.quit()