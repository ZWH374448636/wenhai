from selenium import webdriver
import time

url = "file:///C:/Users/dell/Desktop/test.html"
driver = webdriver.Chrome()
driver.get(url)
# time.sleep(5)
# driver.find_element_by_id("alert").click()
# time.sleep(3)
#切换到alert弹框上
# s = driver.switch_to_alert()
# print(s.text)
#点击警告框确认按钮
# s.accept()

#切换到confirm弹框上
time.sleep(4)
driver.find_element_by_id("confirm").click()
time.sleep(3)
s1 = driver.switch_to_alert()
print(s1.text)
s1.dismiss()
