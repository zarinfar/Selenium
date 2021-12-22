from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BaseURL = "https://testautomation-playground.herokuapp.com/"
driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#driver.get("https://www.google.com/")
#search_value = driver.find_element('name', 'q')
#search_value.send_keys("Keep it Simple Stupid")
#search_value.send_keys(Keys.RETURN)
#driver.get("https://Google.com")
#driver.get(f"{BaseURL}/forms.html")
#driver.find_element('id', 'check_python').click()
#check1 = driver.find_element('id', 'check_validate').text
#assert check1 == "PYTHON"
#text1 = "Amin Zarinfar"
#driver.find_element('id', 'notes').send_keys(text1)
#Check2 = driver.find_element('id', 'area_notes_validate').text
#assert Check2 == text1

#driver.get(f"{BaseURL}/login.html")
#driver.find_element('id', 'user').send_keys('admin')
#driver.find_element('id', 'password').send_keys('admin')
#driver.find_element('id', 'login').click()
#driver.find_element('id', 'green_olive').click()
#driver.find_element('id', 'quantity').send_keys("")
#driver.find_element('id', 'submit_button').click()

driver.get("https://portal.dev.superpay.com.tr/en/users/login/")
driver.find_element('name', 'username').send_keys('m.zarinfar@asanpardakht.ir')
driver.find_element('name', 'password').send_keys('Manualtester13168@!@!')
driver.find_element('name', 'captcha_1').send_keys('ssss')
driver.find_element('id', 'remember').click()
driver.find_element_by_css_selector('#login-form > div.container-login-form-btn > button').click()
Check3 = ""
const Capcha_text = driver.find_element('id', 'container-login__message').text
assert Check3 == Capcha_text


