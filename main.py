from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


url = 'http://shop.danawa.com/main/?controller=goods&methods=search&keyword=%EB%AA%A8%EB%8B%88%ED%84%B0'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 자동으로 크롬드라이버 설치
driver.get(url)
driver.maximize_window()
time.sleep(1)

items = driver.find_element(By.CSS_SELECTOR,"#searchResultView > div.search_main_box.main_prodlist.main_prodlist_list > ul")
time.sleep(10)
# search_box = driver.find_element(By.ID,'query')
# search_box.send_keys(query)
# search_box.send_keys(Keys.ENTER)
# time.sleep(10)