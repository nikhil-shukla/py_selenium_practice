import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
time.sleep(2)
driver.switch_to.frame(driver.find_elements(By.CSS_SELECTOR,'iframe#iframeResult')[0])

text = driver.find_element(By.XPATH,"//h1[contains(text(),'The iframe element')]").text
print('before: ', text)
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@title]"))
driver.find_element(By.XPATH,"//a[@id='w3loginbtn']").click()
driver.switch_to.parent_frame()
text = driver.find_element(By.XPATH,"//h1[contains(text(),'The iframe element')]").text
print('after: ', text)
driver.switch_to.default_content()
# driver.switch_to.parent_frame() both holds good - default content & parent_frame & driver.switch_to.window(driver.window_handles[0])
size = driver.find_element(By.CSS_SELECTOR,'span#framesize').text
print(size)

frames = driver.find_elements(By.TAG_NAME,'iframe')
for frame in frames:
    print(frame.get_attribute("id"))

driver.switch_to.new_window('tab')
driver.get("https://www.inviul.com/getwindowhandle-window-switching/")
# driver.execute_script()
actions = ActionChains(driver)
actions.move_to_element(driver.find_element(By.XPATH,"//span[contains(text(),'Hit Me')]")).perform()
driver.find_element(By.XPATH,"//span[contains(text(),'Hit Me')]").click()
parentWindow = driver.current_window_handle
print(parentWindow)
windows=driver.window_handles
for window in windows:
    if window != parentWindow:
        driver.switch_to.window(window)
    else:
        pass
    print(window)