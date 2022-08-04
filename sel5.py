import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager

path = './screenshots/'


def capture_snap(d, p):
    filename = "snap_" + time.asctime().replace(':', '_') + ".png"
    d.save_screenshot(p + filename)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/windows")
wait = WebDriverWait(driver, 10)
# lists = driver.find_elements(By.XPATH, '//ul/li')
# for li in lists:
#     print(li.text)
#     if li.text == 'Multiple Windows':
#         actions = ActionChains(driver)
#         actions.move_to_element(li).click().perform()
#         time.sleep(2)
#         break
# try:
#     driver.switch_to.window(driver.window_handles[1])
#     capture_snap(driver, './screenshots/')
# except Exception:
#     capture_snap(driver, './screenshots/')

wait.until(ec.presence_of_element_located((By.XPATH, "//h3[contains(text(),'Opening')]")))
# new_url = driver.current_url
# print(new_url)
capture_snap(driver, path)

driver.find_element(By.LINK_TEXT, 'Click Here').click()

driver.switch_to.window(driver.window_handles[1])

text = driver.find_element(By.XPATH, '//h3').text
print(text)

capture_snap(driver, path)

driver.quit()