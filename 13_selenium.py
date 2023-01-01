from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

url = 'https://www.naver.com/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # 자동으로 크롬드라이버 설치
driver.get(url)
driver.maximize_window()
time.sleep(1)

try:
    elem = WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.XPATH,"값"))) # max 10sec
finally:
    driver.quit()

# 지정한 위치로 스크롤 내리기 with javascript
# driver.execute_script("window.scrollTo(0, 1080)")

# 화면 가장 아래로 스크롤 내리기
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 현재 문서 높이 가져오기
# prev_height = driver.execute_script(("return document.body.scrollHeight"))

# driver.page_source 페이지 소스

# headless Chrome
# options = webdriver.ChromeOptions()
# options.headless = True
# options.add_argument("window-size = 1920x1080")
# browser = webdriver.Chrome(options=options)

# driver.get_screenshot_as_file("value.png")