from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(20)
#定位select里的选项第一种方式：二次定位
#先定位select框，再定位select里的选项

mouse = driver.find_element_by_link_text("设置")
ActionChains(driver).move_to_element(mouse).perform()
#点击搜索设置
driver.find_element_by_link_text("搜索设置").click()

#分两步，先定位下拉框再定位选项
s = driver.find_element_by_id("nr")
# s.find_element_by_xpath("//option[@value='50']").click()
#通过索引：select_by_index()
Select(s).select_by_value("20")
# re = Select(s).select_by_value(1)
# print(re)
