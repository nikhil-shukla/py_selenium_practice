import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("debuggerAddress","localhost:9222")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_opt)
# driver.get("https://www.espn.in/soccer/table/_/league/eng.1")
# driver.implicitly_wait(2)
# driver.maximize_window()

driver.find_element(By.XPATH,"//span[text()='Teams']").click()
print(driver.find_element(By.XPATH,"//span[text()='Teams']").value_of_css_property("font-size"))