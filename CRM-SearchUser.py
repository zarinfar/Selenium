from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")

# Signin
driver.get("https://portal.dev.superpay.com.tr/en/users/login/?nocaptcha=true")
driver.find_element('name', 'username').send_keys('m.zarinfar@asanpardakht.ir')
sleep(1)
driver.find_element('name', 'password').send_keys('Manualtester13168@!@!')
sleep(1)
driver.find_element('id', 'remember').click()
sleep(2)
driver.find_element('xpath', '//*[@id="login-form"]/div[4]/button').click()
print('Login was successful')
sleep(12)

# Select CRM Menu
driver.find_element('xpath', '/html/body/main/div/div/div[2]/ul/li[2]/div/div[3]/a').click()
print('Successfully CRM opened')
sleep(10)

# Case 1: Enter Empty
driver.find_element('id', 'phoneNumber').send_keys('')
driver.find_element('xpath', '//*[@id="content"]/div/form/div/div[3]/button').click()
message1 = "mobile number is not valid"
message2 = driver.find_element('css selector', '#content > div > form > div:nth-child(2)').text
assert message2 == message1
print('Case 1 (Enter Empty) was successful')
sleep(3)
# Case 2: Enter Space
driver.find_element('id', 'phoneNumber').send_keys('   ')
driver.find_element('xpath', '//*[@id="content"]/div/form/div/div[3]/button').click()
message1 = "mobile number is not valid"
message3 = driver.find_element('css selector', '#content > div > form > div:nth-child(2)').text
assert message3 == message1
print('Case 2 (Enter Space) was successful')
sleep(3)
# Case 3: Enter Wrong number
driver.find_element('id', 'phoneNumber').send_keys('055')
driver.find_element('xpath', '//*[@id="content"]/div/form/div/div[3]/button').click()
message1 = "mobile number is not valid"
message4 = driver.find_element('css selector', '#content > div > form > div:nth-child(2)').text
assert message4 == message1
print('Case 3 (Enter Wrong number) was successful')
sleep(5)

# Case 4: Enter Valid number but NOT Registered
driver.find_element('id', 'phoneNumber').clear()
driver.find_element('id', 'phoneNumber').send_keys('905550000055')
driver.find_element('xpath', '//*[@id="content"]/div/form/div/div[3]/button').click()
message5 = "phone number not registered"
message6 = driver.find_element('css selector', '#content > div > form > div:nth-child(2)').text
assert message6 == message5
print('Case 4 ( Enter Valid number but NOT Registered) was successful')
sleep(5)

# Case 5: Enter Valid number
driver.find_element('id', 'phoneNumber').clear()
driver.find_element('id', 'phoneNumber').send_keys('905550000009')
driver.find_element('xpath', '//*[@id="content"]/div/form/div/div[3]/button').click()
sleep(5)
thephone = "05550000009"
checkphone = driver.find_element('xpath', '//*[@id="content"]/div[2]/div[1]/div[2]/p[2]').text
assert checkphone == thephone
print('Case 5 (Enter Valid number) was successful')
sleep(5)
driver.quit()
