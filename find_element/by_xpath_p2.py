from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")
sleep(2)

# driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys("51zxw")
driver.find_element_by_xpath("//input[@type='text' and @name='username' ]").send_keys("51zxw11")
sleep(2)
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys("51zxw")


