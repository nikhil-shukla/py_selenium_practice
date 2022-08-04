import time
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager


def is_element_present(how, what):
    if len(driver.find_elements(by=how, value= what))==0:
        return False
    else:
        return True


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')
print(is_element_present(By.XPATH, '//div[4]/input[1]'))
driver.implicitly_wait(1)
# driver.find_element(By.XPATH, '//div[4]/input[1]').click()
# print(is_element_present(By.XPATH, '//div[4]/input[1]'))
# driver.find_element(By.XPATH, '//div[4]/input[2]').click()
# driver.find_element(By.XPATH, '//div[4]/input[3]').click()
# driver.find_element(By.XPATH, '//div[4]/input[4]').click()


block = driver.find_element(By.XPATH,"/html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")
checkboxes = block.find_elements(By.NAME,"sports")

for checkbox in checkboxes:
    if checkbox.is_selected():
        pass
    else:
        checkbox.click()

print("total checkboxes: ",len(checkboxes) )
driver.close()
