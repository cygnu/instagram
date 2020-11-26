from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import os

import settings


# Chromeを起動させる
options = Options()
driver = webdriver.Chrome(options=options)

url = 'https://www.instagram.com/nikkei_business_official/'
driver.get(url)

def login_instagram():
    # ログイン処理
    driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
    time.sleep(5)
    driver.find_element_by_name('username').send_keys(settings.USER_NAME)
    driver.find_element_by_name('password').send_keys(settings.PASSWORD)
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(5)
    
    driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()


def download_instagram():
    # パス(保存先)が存在しなければ新規作成
    path = './img/'
    if not os.path.exists(path):
        os.mkdir(path)

    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()
    time.sleep(5)

    for i in range(10):
        image_url = driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[2]/div/div/div[1]/img').get_attribute('src')
        image_name = path + 'image{0}.jpg'.format(i)
        urllib.request.urlretrieve(image_url, image_name)
        time.sleep(1)
        driver.find_element_by_class_name('_65Bje.coreSpriteRightPaginationArrow').click()
        time.sleep(1)

    driver.quit()

if __name__ == "__main__":
    login_instagram()
    download_instagram()