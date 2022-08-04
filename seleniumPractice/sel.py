import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://pypi.org')
# time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='search']").send_keys('selenium')
# time.sleep(2)
WebDriverWait(driver,5).until(ec.element_to_be_clickable((By.XPATH,"//input[@id='search']")))
driver.find_element('xpath',"//input[@id='search']").send_keys('wdm')
# time.sleep(2)

driver.switch_to.new_window('tab')
driver.get('https://www.wikipedia.org/')
dropdown = driver.find_element('id','searchLanguage')
select = Select(dropdown)
select.select_by_value('hi')
# time.sleep(2)
for i in select.options:
    print(i.text)
print(len(select.options))

links = driver.find_elements(By.TAG_NAME,'a')
print(len(links))
for url in links:
    print(url.get_attribute('href'))
driver.quit()
