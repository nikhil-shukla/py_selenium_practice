import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_opt = webdriver.ChromeOptions()
prefs = {"profile.default_content_Setting_values.notification":2}
chrome_opt.add_experimental_option("prefs",prefs)
chrome_opt.headless = False

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_opt)
driver.get("https://www.espn.in/soccer/table/_/league/eng.1")
driver.implicitly_wait(2)
driver.maximize_window()
print(driver.title)
time.sleep(5)
r = driver.find_elements(By.XPATH,'//tbody/tr')
c= driver.find_elements(By.XPATH,'//tbody/tr[1]/td')
rows = len(r)
cols = len(c)
print(rows, ' & ', cols)

for row in range(1, rows):
    for col in range(1,cols):
        print(driver.find_element(By.XPATH,f'//tbody/tr[{row}]/td[{col}]').text, end=' ')
    print()


S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
driver.set_window_size(S('Width'),S('Height'))
driver.find_element(By.TAG_NAME,'body').screenshot('./screenshots/fullpage.png')
driver.close()