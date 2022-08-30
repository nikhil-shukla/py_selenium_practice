import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as es


@pytest.fixture(scope='function', params=['chrome', 'edge'])
def get_browser(request):
    if request.params=='chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.params=='edge':
        driver = webdriver.Edge(service=es(EdgeChromiumDriverManager().install()))
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    yield driver
    driver.quit()

