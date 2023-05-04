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
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin


def main():
    options = webdriver.ChromeOptions()
    browser = webdriver.Chrome()
    actions = ActionChains(browser)
    #browser.set_window_size(800, 600)
    browser.maximize_window()    
    browser.get('https://resortofhelling.netlify.app/')

    #Проверка видимости заголовка страницы
    #header = browser.find_element(By.XPATH, '//h1[contains(.,"Семь Кругов Ада")]').is_displayed()

    #Проверка наличия фото Жукова
    #serega = browser.find_element(By.XPATH, '//tr[5]/td[2]').is_displayed()

    #Проверка  количества блоков приветсвенного текста
    #amountOfTextBlocks = browser.find_elements(By.XPATH, '//div[1]/p')
    #assert len(amountOfTextBlocks) == 6
    #print("OK - amountOfTextBlocks is 6")
    
    #Проверка количества круглых значков
    #numberOfSights = browser.find_elements(By.XPATH, '//a/img')
    #assert len(numberOfSights) == 4
    #print("OK - numberOfSights is 4")

    #Проверка количества картинок в таблице Услуг
    #amountOfService = browser.find_elements(By.XPATH, '//tbody[2]/tr/td/img')
    #assert len(amountOfService) == 7
    #print("OK - amountOfService is 7")

    #Проверка количества картинок на странице
    #numberOfImg = browser.find_elements(By.XPATH, '//img')
    #assert len(numberOfImg) == 23
    #print("ОK - numberOfImg is 23")

    #Функционирование элемента slider и выставленеи значения 860
    #donate = browser.find_element(By.XPATH, '//input[@name="amountMoney"]')
    #move = ActionChains(browser)
    #move.click_and_hold(donate).move_by_offset(133, 0).release().perform()

    #Нажатие кнопки Поддать дров
    #pushDonate = browser.find_element(By.XPATH, '//input[@name="isubmit"]').click()
    #time.sleep(5)

    #Ввод текста в Анкету
    #insertName = browser.find_element(By.XPATH, '//input[@name="hisname"]').send_keys("Квазиморд Витальевич")
    #insertAge = browser.find_element(By.XPATH, '//input[@name="age"]').send_keys(98)

    #Проверка активности чек-бокса Шоу и активация другого чек-бокса Орешки
    #checkedChekbox = browser.find_element(By.XPATH, '//p/input[3]').is_selected()
    #selectCheckbox = browser.find_element(By.XPATH, '//p/input[4]').click()

    # Выбор опции Шаманист из выпадающего списка богов
    #godChoising = browser.find_element(By.XPATH, '//select[@name="god"]')
    #select = Select(godChoising)
    #select.select_by_visible_text("Шаманист")

    #Ввод текста в текстовое поле О госте
    #typeText = browser.find_element(By.XPATH, '//textarea').send_keys("Трёшка на Парнасе...я наследник, а он всё никак!!! ЫЫыы!!\n")

    #Нажатие кнопки Знайте же
    #pushKnowThis = browser.find_element(By.XPATH, '//input[@name="getinfo"]').click()

    #Проверка наличия текста Пьяницы в словах льва
    #lionsTale = browser.find_element(By.XPATH, '//td[contains(text(), "пьяницы")]')
    #textLion = lionsTale.text
    #assert "пьяницы" in textLion
    #print('Лев не врёт')

    # Работа фрейма видеоплеера
    videoFrame = browser.find_element(By.TAG_NAME, "iframe")
    actions.move_to_element(videoFrame)
    actions.perform()
    browser.switch_to.frame(videoFrame)
    playMovie = browser.find_element(By.CSS_SELECTOR, '.ytp-large-play-button').click()
    time.sleep(11)
    pauseMovie = browser.find_element(By.CSS_SELECTOR, '.ytp-play-button').click()
    browser.switch_to.default_content()


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
