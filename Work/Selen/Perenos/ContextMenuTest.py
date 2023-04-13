from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

def Start():
#Измените строку, для выполнения теста в другом браузере
    chrome_options = Options()
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://www.google.com/')
    
#def InputText():
    browser.implicitly_wait(4)
    browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys('World of tanks')
    
#def PushButton():
    browser.find_element(By.CSS_SELECTOR, '[name="btnK"]').click()
    
#def ClearField(:
    browser.find_element(By.CSS_SELECTOR, '[name="q"]').clear()
    browser.find_element(By.CSS_SELECTOR, '[name="q"]').send_keys("World of ")
    
#def NumberOfOptions():
    #OptionsInList = browser.find_elements(By.XPATH,'//div[@class="lnnVSe" and @role="option" and @aria-description]')

    #assert int(len(OptionsInList)) == 10
    
    
#def FirstIsImage():
    HeadTextOnFirst = browser.find_element(By.XPATH,'(//span[contains(text(), "world of tanks")])[1]').is_displayed()
    ImageOnfirst = browser.find_element(By.XPATH,'(//div[contains(@class, "sbic")])[1]').is_displayed()
    SmallTextOnFirst = browser.find_element(By.XPATH, "(//*[contains(text(), 'World of — Серия видеоигр')])[1]").is_displayed()
    assert HeadTextOnFirst == True and ImageOnfirst == True and SmallTextOnFirst == True
    
#def IsFive():
    #browser.implicitly_wait(4)
    #ListOfAdjustments = browser.find_elements(By.XPATH,'//div[@class="sbic sb43"]')
    
    #assert int(len(ListOfAdjustments)) == 5
    
#def step(context, text):
    #WebDriverWait(context.browser, 120).until(
        #EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % text))
    #)
    #assert context.browser.find_element(By.XPATH,'//*[contains(text(), "%s")]' % text)

Start()