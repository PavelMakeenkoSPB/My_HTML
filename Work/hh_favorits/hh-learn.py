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

# waitingPage = wait.until(element_located((By.XPATH,"//input[@id='text']"))).send_keys('beer')
# buttonS = find_element(By.XPATH,"//button[contains(text(),'Найти')]").click()
# time.sleep(20)
# time.sleep(5)
# waitingPage = wait.until(element_located((By.XPATH, '//span[contains(text(),"Продолжить")]')))
with_pass = find_element(By.XPATH, "//button[contains(text(),'Войти с паролем')]").click()
# tap = find_element(By.XPATH,'//span[contains(text(),"Продолжить")]').click()
login = find_element(By.XPATH, "//input[@placeholder='Электронная почта или телефон']").send_keys('ptg@bk.ru')
pas = find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('3ebb8Ye5')
entering = find_element(By.XPATH, "//span[contains(text(),'Войти')]").click()
time.sleep(1)

find_all = browser.find_elements(By.XPATH,"(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] )")
kol_vo = len(find_all)

mass =[]
for i in range(1, kol_vo + 1, 1):
    st = str(i)
    xpath_Upd = '"' + "(" + "//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] )" + "[" + st + "]" + '"'
    mass.append(xpath_Upd)

for r in range(0, 20, 1):
    # element = find_element(By.XPATH, mass[r])
    element =  mass[r]
    print(element)
#     browser.execute_script("arguments[0].scrollIntoView();", element)
#     browser.execute_script("arguments[0].click();", element)
# print('Fav_20 -untapped')



# Это всё работает
# element = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [1]")
# #
# # # Прокрутить до элемента
# browser.execute_script("arguments[0].scrollIntoView();", element)
# #
# # # Нажать на элемент с помощью JavaScript
# browser.execute_script("arguments[0].click();", element)
# print('Fav_1 -untapped')
#
#
# element2 = find_element(By.XPATH, "(//button [contains (@data-qa,'vacancy-search-mark-favorite_true') ] ) [2]")
# #
# # # Прокрутить до элемента
# browser.execute_script("arguments[0].scrollIntoView();", element2)
# #
# # # Нажать на элемент с помощью JavaScript
# browser.execute_script("arguments[0].click();", element2)
# print('Fav_2 -untapped')
# Вот до сюда работает








# wait.until(element_located((By.XPATH, "(//button [contains (@data-qa,'favorite_true_narrow') ] ) [2]")))
# cl = find_element(By.XPATH, "(//button [contains (@data-qa,'favorite_true_narrow') ] ) [2]")
# browser.implicitly_wait(2)
# cl.click()

# WebDriverWait(browser, 2).until(EC.presence_of_all_elements_located)
# element = find_element(By.XPATH, "(//button [contains (@data-qa,'favorite_true_narrow') ] ) [1]").click()
# browser.implicitly_wait(1)
# actions.move_to_element(element).click(element).double_click(element).perform()






# arr = []
# elo = []
# for i in range(1, 21):
#     st = str(i)
#     xpath_Upd = '"' + "(" + "//button [contains (@data-qa,'favorite_true_narrow') ] )" + "[" + st + "]" + '"'
#     arr.append(xpath_Upd)
#     elementos = 'find_element(By.XPATH,' + f'{xpath_Upd}'+')'
#     elo.append(elementos)
#     # print (elemento)
#
#
# # #
# for k in range(0, 20, 1):
# #
# #     # print (arr[k])
# #
#     # element = find_element(By.XPATH, (f'{arr[k]}'))
# #     print (element)
#     tap = elo[k]
#     print (tap)
#     browser.implicitly_wait(1)
#     browser.execute_script("arguments[0].scrollIntoView();", tap)
#     browser.implicitly_wait(1)
#     browser.execute_script("arguments[0].click();", tap)
# print('All Favs was clicked')
#
# time.sleep(2)


# arr = []
# for i in range(1, 58):
#     st = str(i)
#     xpathUpdate = "(" + '//img[contains(@src, "material-picture.png")]' + ')' + '[' + st + "]"
#     arr.append(xpathUpdate)
#
# time.sleep(2)
# for k in range(len(arr)):
#     downloadMat = browser.find_element(By.XPATH, arr[k]).click()


# fav = find_element(By.XPATH, "//span[contains(text(),'В начало')]").click()
# row4 = find_element(By.XPATH, "//span[contains(text(),'3')]").click()

# (//button [contains (@data-qa,'favorite_true_narrow') ] ) [4]
#
# for i in range(1,20,1):
#     find_element (By.XPATH, "(//button [contains (@data-qa,'favorite_true_narrow') ] ) [i]" ).click()