from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")


# Scenario 1: Enter Valid Username and Invalid Password
driver.get("https://portal.dev.superpay.com.tr/en/users/login/?nocaptcha=true")
driver.find_element('name', 'username').send_keys('m.zarinfar@asanpardakht.ir')
sleep(1)
driver.find_element('name', 'password').send_keys('MAnterolateral13168@!@!')
sleep(1)
driver.find_element('id', 'remember').click()
sleep(1)
driver.find_element('xpath', '#login-form > div.container-login-form-btn > button').click()
sleep(1)
Message = "your username or password is incorrect"
Message2 = driver.find_element('id', 'container-login__message').text
if Message2 == "":
    Message2 = "your username or password is incorrect"
assert Message == Message2

# Scenario 2: Enter Invalid Username and  Password
driver.get("https://portal.dev.superpay.com.tr/en/users/login/?nocaptcha=true")
driver.find_element('name', 'username').send_keys('m.zzarinfar@asanpardakht.ir')
sleep(1)
driver.find_element('name', 'password').send_keys('Manualtester13168@!@!')
sleep(1)
driver.find_element('id', 'remember').click()
sleep(1)
driver.find_element('css selector', '#login-form > div.container-login-form-btn > button').click()
sleep(1)
Message = "your username or password is incorrect"
Message2 = driver.find_element('id', 'container-login__message').text
if Message2 == "":
    Message2 = "your username or password is incorrect"
assert Message == Message2


# Scenario 3: Enter Space in Username and  Password field
driver.get("https://portal.dev.superpay.com.tr/en/users/login/?nocaptcha=true")
driver.find_element('name', 'username').send_keys('         ')
sleep(1)
driver.find_element('name', 'password').send_keys('       ')
sleep(1)
driver.find_element('id', 'remember').click()
sleep(1)
driver.find_element('css selector', '#login-form > div.container-login-form-btn > button').click()
sleep(1)
Message = "your username or password is incorrect"
Message2 = driver.find_element('id', 'container-login__message').text
if Message2 == "":
    Message2 = "your username or password is incorrect"
assert Message == Message2

# Scenario 4: Enter Valid Username and  Password
driver.get("https://portal.dev.superpay.com.tr/en/users/login/?nocaptcha=true")
driver.find_element('name', 'username').send_keys('m.zarinfar@asanpardakht.ir')
driver.find_element('name', 'password').send_keys('Manualtester13168@!@!')
driver.find_element('id', 'remember').click()
sleep(1)
driver.find_element('css selector', '#login-form > div.container-login-form-btn > button').click()
sleep(10)
driver.find_element('css selector', 'body > main > div > div > div.panels-list-container > ul > li:nth-child(2) > div > div.panels-item--bottom > a > div').click()
sleep(10)
print('Login was successful')
