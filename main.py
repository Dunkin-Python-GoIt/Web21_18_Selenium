from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 


ch_options = Options()
ch_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=ch_options)
driver.get('https://realpython.com')
# with open("new_data.html", "w", encoding="utf-8") as f:
#     f.write(driver.page_source)
inputs = driver.find_elements(By.XPATH, "//input[@class='search-autocomplete search-field form-control form-control-md mr-sm-1 mr-lg-2 w-100']")

for in_ in inputs:
    in_.send_keys("Hello")

sleep(100)
# driver.quit()