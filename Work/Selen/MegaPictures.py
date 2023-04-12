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

def main():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")    
    browser = webdriver.Chrome()
    browser.maximize_window()    
    browser.get('file:///C:/temp/QA/Git/My_HTML/Work/first.html')
    browser.delete_all_cookies()
    actions = ActionChains(browser)
    actions.send_keys(Keys.F12).perform()
    browser.FindElement(By.TagName("body")).SendKeys(Keys.F12)

    try:

        element = WebDriverWait(browser, 50).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
    except:
        numb = browser.find_element(By.XPATH, '//*[@name="btn"]').click()
    try:
        elem = WebDriverWait(driver, 60).until(lambda driver: driver.execute_script("return document.readyState").equals("complete"))

    except:
        browser.quit()
        print('FINE')
main()