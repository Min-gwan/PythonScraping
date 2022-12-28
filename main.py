from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
query = input('검색할 키워드를 입력하세요')

url = 'https://www.naver.com/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.ID,'query')
search_box.send_keys(query)
search_box.send_keys(Keys.ENTER)
time.sleep(10)