import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
waitingPage = wait.until(element_located((By.XPATH, '//span[contains(text(),"Продолжить")]')))
with_pass = find_element(By.XPATH, "//button[contains(text(),'Войти с паролем')]").click()
# tap = find_element(By.XPATH,'//span[contains(text(),"Продолжить")]').click()
login = find_element(By.XPATH, "//input[@placeholder='Электронная почта или телефон']").send_keys('ptg@bk.ru')
pas = find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('3ebb8Ye5')
entering = find_element(By.XPATH, "//span[contains(text(),'Войти')]").click()
time.sleep(1)


arr = []
for i in range(1, 20):
    st = str(i)
    xpath_Upd = "(" + "//button [contains (@data-qa,'favorite_true_narrow') ] )" + "[" + st + "]"
    arr.append(xpath_Upd)


for k in range(1,20):
   test =  find_element(By.XPATH, arr[k]).click()
   print(test)

time.sleep(10)
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