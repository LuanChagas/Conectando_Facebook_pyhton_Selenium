from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

option = Options()
option.set_preference('dom.push.enabled', False)
driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe',firefox_options=option)
driver.get("http://www.facebook.com")
elem = driver.find_element_by_name("email")
print(elem)
elem.send_keys("Seu Email")
elem = driver.find_element_by_name("pass")
elem.send_keys("Sua Senha")
elem.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
elem = driver.find_element_by_name("xhpc_message")
elem.send_keys("Post Test usando Python - Selenium 🐍")
driver.implicitly_wait(10)
elem = driver.find_element_by_css_selector("._1mf7").click()
print(elem)

