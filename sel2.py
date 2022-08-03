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
    try:
        driver.find_element(by=how,value=what)
        return True
    except NoSuchElementException:
        return False


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('http://www.tizag.com/htmlT/htmlcheckboxes.php')
print(is_element_present(By.XPATH, '//div[4]/input[1]'))
# driver.find_element(By.XPATH, '//div[4]/input[1]').click()
# print(is_element_present(By.XPATH, '//div[4]/input[1]'))
# driver.find_element(By.XPATH, '//div[4]/input[2]').click()
# driver.find_element(By.XPATH, '//div[4]/input[3]').click()
# driver.find_element(By.XPATH, '//div[4]/input[4]').click()

i = 1

while is_element_present(By.XPATH, f"//div[4]/input['{str(i)}']"):
    driver.find_element(By.XPATH, f"//div[4]/input['{str(i)}']").click()
    i += 1

driver.close()
