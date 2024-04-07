import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
actions = ActionChains(browser)
wait = WebDriverWait(browser, 1)
element_located = EC.presence_of_element_located
find_element = browser.find_element

browser.maximize_window()
browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=3')


with_pass = find_element(By.XPATH, "//button[contains(text(),'Войти с паролем')]").click()

login = find_element(By.XPATH, "//input[@placeholder='Электронная почта или телефон']").send_keys('ptg@bk.ru')
pas = find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('3ebb8Ye5')
entering = find_element(By.XPATH, "//span[contains(text(),'Войти')]").click()
time.sleep(1)

def unfavor():
    element1 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [1]")
    # Прокрутить до элемента
    browser.execute_script("arguments[0].scrollIntoView();", element1)
    #
    # # Нажать на элемент с помощью JavaScript
    browser.execute_script("arguments[0].click();", element1)
    print('Fav_1 -untapped')

    time.sleep(1)
    element2 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [2]")
    #
    # # Прокрутить до элемента
    browser.execute_script("arguments[0].scrollIntoView();", element2)
    #
    # # Нажать на элемент с помощью JavaScript
    browser.execute_script("arguments[0].click();", element2)
    print('Fav_2 -untapped')
    time.sleep(1)
    element3 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [3]")
    browser.execute_script("arguments[0].scrollIntoView();", element3)
    browser.execute_script("arguments[0].click();", element3)
    print('Fav_3 -untapped')
    time.sleep(1)
    element4 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [4]")
    browser.execute_script("arguments[0].scrollIntoView();", element4)
    browser.execute_script("arguments[0].click();", element4)
    print('Fav_4 -untapped')
    time.sleep(1)
    element5 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [5]")
    browser.execute_script("arguments[0].scrollIntoView();", element5)
    browser.execute_script("arguments[0].click();", element5)
    print('Fav_5 -untapped')
    time.sleep(1)
    element6 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [6]")
    browser.execute_script("arguments[0].scrollIntoView();", element6)
    browser.execute_script("arguments[0].click();", element6)
    print('Fav_6 -untapped')
    time.sleep(1)
    element7 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [7]")
    browser.execute_script("arguments[0].scrollIntoView();", element7)
    browser.execute_script("arguments[0].click();", element7)
    print('Fav_7 -untapped')
    time.sleep(1)
    element8 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [8]")
    browser.execute_script("arguments[0].scrollIntoView();", element8)
    browser.execute_script("arguments[0].click();", element8)
    print('Fav_8 -untapped')
    time.sleep(1)
    element9 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [9]")
    browser.execute_script("arguments[0].scrollIntoView();", element9)
    browser.execute_script("arguments[0].click();", element9)
    print('Fav_9 -untapped')
    time.sleep(1)
    element10 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [10]")
    browser.execute_script("arguments[0].scrollIntoView();", element10)
    browser.execute_script("arguments[0].click();", element10)
    print('Fav_10 -untapped')
    time.sleep(1)


unfavor()
print('Page 3 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=4')
unfavor()
print('Page 4 Done')
#
browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=5')
unfavor()
print('Page 5 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=6')
unfavor()
print('Page 6 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=7')
unfavor()
print('Page 7 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=8')
unfavor()
print('Page 8 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=9')
unfavor()
print('Page 9 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=10')
unfavor()
print('Page 10 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=11')
unfavor()
print('Page 11 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=12')
unfavor()
print('Page 12 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=13')
unfavor()
print('Page 13 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=14')
unfavor()
print('Page 14 Done')

browser.get('https://spb.hh.ru/applicant/favorite_vacancies?page=15')
unfavor()
print('Page 15 Done')
