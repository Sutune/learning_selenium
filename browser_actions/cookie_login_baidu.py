from  selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")

#add cookie。
driver.add_cookie({'name':'BAIDUID','value':'3305D8BF7C3A873E81C4B8AB3D754E42:FG=1'})
driver.add_cookie(({'name':'BDUSS','value':'ZPWkI5bnJLb2IyRGhhVzB6dmpwSlVWZ3AxSTlaWkxLTVBhdkZWV1JNRkFwcHBaSVFBQUFBJCQAAAAAAAAAAAEAAAAoZz4Sc2h1YmFpMjAxMQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAZc1lAGXNZYT'}))

sleep(3)
driver.refresh()

sleep(3)
driver.quit()