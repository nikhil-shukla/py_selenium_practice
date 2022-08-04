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

wait = WebDriverWait(driver,10)
driver.get("https://automatenow.io/sandbox-automation-testing-practice-website/slider/")
ele = driver.find_element(By.CSS_SELECTOR, '#slideMe')
loc = ele.location
print(loc)
size = ele.size
print(size)
w,h =size['width'],size['height']
print(w,h)
action = ActionChains(driver)
action.drag_and_drop_by_offset(ele, w/5, 0).perform()
time.sleep(2)

driver.switch_to.new_window('tab')
driver.get("https://deluxe-menu.com/popup-mode-sample.html")
wait.until(ec.visibility_of_element_located((By.XPATH,'//p[2]/img')))
img = driver.find_element(By.XPATH,'//p[2]/img')
action.context_click(img).perform()
product=driver.find_element(By.CSS_SELECTOR,"#dm2m1i1tdT")
action.move_to_element(product).perform()
time.sleep(3)