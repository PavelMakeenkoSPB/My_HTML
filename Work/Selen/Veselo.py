from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://www.google.com/")
    browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('Terminator')
    browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()

main()
