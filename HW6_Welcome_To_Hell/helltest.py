import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

def main():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    #browser.set_window_size(800, 600)
    browser.maximize_window()    
    browser.get('https://resortofhelling.netlify.app/')
    
    #header = browser.find_element(By.XPATH, '//h1[contains(.,"Семь Кругов Ада")]').is_displayed()
    #serega = browser.find_element(By.XPATH, '//tr[5]/td[2]').is_displayed()

    #amountOfTextBlocks = browser.find_elements(By.XPATH, '//div[1]/p')
    #assert len(amountOfTextBlocks) == 6
    #print("OK - amountOfTextBlocks is 6")

    #numberOfSights = browser.find_elements(By.XPATH, '//a/img')
    #assert len(numberOfSights) == 4
    #print("OK - numberOfSights is 4")

    #amountOfService = browser.find_elements(By.XPATH, '//tbody[2]/tr/td/img')
    #assert len(amountOfService) == 7
    #print("OK - amountOfService is 7")

    #numberOfImg = browser.find_elements(By.XPATH, '//img')
    #assert len(numberOfImg) == 23
    #print("ОK - numberOfImg is 23")
    
    #donate = browser.find_element(By.XPATH, '//input[@name="amountMoney"]')
    #move = ActionChains(browser)
    #move.click_and_hold(donate).move_by_offset(133, 0).release().perform()

    #pushDonate = browser.find_element(By.XPATH, '//input[@name="isubmit"]').click()
    #time.sleep(5)

    insertName = browser.find_element(By.XPATH, '//input[@name="hisname"]').send_keys("Квазиморд Витальевич")
    
    insertAge = browser.find_element(By.XPATH, '//input[@name="age"]').send_keys(98)
    
    checkedChekbox = browser.find_element(By.XPATH, '//p/input[3]').is_selected()

    selectCheckbox = browser.find_element(By.XPATH, '//p/input[4]').click()

    godChoising = browser.find_element(By.XPATH, '//select[@name="god"]')
    select = Select(godChoising)
    select.select_by_visible_text("Шаманист")
    
    typeText = browser.find_element(By.XPATH, '//textarea').send_keys("Трёшка на Парнасе...я наследник, а он всё никак!!! ЫЫыы!!\n")

    pushKnowThis = browser.find_element(By.XPATH, '//input[@name="getinfo"]').click()

    lionsTale = browser.find_element(By.XPATH, '//td[contains(text(), "пьяницы")]')
    textLion = lionsTale.text
    assert "пьяницы" in textLion
    print('Лев не врёт')


    time.sleep(10)
  
  # browser.quit()

    # try:

        # element = WebDriverWait(browser, 30).until(
            #EC.presence_of_element_located((By.ID, "myDynamicElement"))
        # )
    # except:
        #numb = browser.find_element(By.XPATH, '//*[@name="btn"]').click()
    # try:
        #elem = WebDriverWait(driver, 10).until(lambda driver: driver.execute_script("return document.readyState").equals("complete"))

    # except:
        # numb = browser.find_element(By.XPATH, '//*[@name="btn"]').click()  # Прекращает исполнение кода. не закрывая браузер, чтобы была возможность увидеть статус document.readyState -"complete", нужно только для отчёта.
        # browser.quit()
        #print('Test Is Successful!!')
main()
