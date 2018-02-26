from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://bj.ganji.com/")
driver.implicitly_wait(10) #隐式等待
#获取当前窗口的句柄
handle = driver.current_window_handle
print(handle)

#获取所有句柄
driver.find_element_by_link_text("工作").click()
all_handle = driver.window_handles
print(all_handle)

#切换窗口方法1
# for i in all_handle:
#     if i == handle:
#         driver.switch_to.window(i)
#         print(driver.title)

#切换窗口方法2
driver.switch_to.window(all_handle[0])
print(driver.title)
