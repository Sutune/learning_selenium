from login_page import test_user_login
from selenium import webdriver

driver=webdriver.Firefox()

username='51zxw'
password='123456'

test_user_login(driver,username,password)
sleep(3)
driver.quit()