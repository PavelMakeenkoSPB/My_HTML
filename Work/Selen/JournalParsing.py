import time
import parse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from bs4 import BeautifulSoup


options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
actions = ActionChains(browser)
#browser.set_window_size(800, 600)
browser.maximize_window()    
browser.get('https://journal.top-academy.ru/ru/auth/login/index')
actions = ActionChains(browser)

time.sleep(5)
typeLogin = browser.find_element(By.XPATH, '//*[@id="username"]').send_keys("Makee_jv78")

typePass = browser.find_element(By.XPATH, '//*[@id="password"]').send_keys("0Cf5Lt41")

time.sleep(2)
pushEnter = browser.find_element(By.XPATH, '//*[@id="1"]/form/button').click()

time.sleep(5)

bar = browser.find_element(By.XPATH, '//ng-component/div/div[1]/nav/div')
actions(browser).click_and_hold(bar).release().perform()

time.sleep(3)

findMat = browser.find_element(By.XPATH, '//span[contains(text(), "Учебные материалы")]').click()



#Makee_jv78
# 0Cf5Lt41
