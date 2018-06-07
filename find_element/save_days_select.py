from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver=webdriver.Firefox()

driver.get("http://www.51zxw.net")

sleep(2)
#定位下拉框
select=Select(driver.find_element_by_css_selector("[name='CookieDate']"))

# select.select_by_index(1)
# select.select_by_visible_text("留一年")
select.select_by_value("1")

sleep(3)
driver.quit()