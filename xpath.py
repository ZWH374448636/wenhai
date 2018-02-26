from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#xpath模糊匹配功能
driver.find_element_by_xpath("//*[contains(text(),'hao123')]").click()

#xpath模糊匹配某个属性
driver.find_element_by_xpath("//*[contains(@di,'kw')]").click()

#xpath可以模糊匹配以什么开头
driver.find_element_by_xpath("//*[starts-with(@id,'s_kw_')]").click()

#xpath可以模糊匹配以什么结尾
driver.find_element_by_xpath("//*[ends-with(@id,'kw_wrap')]").click()

#xpath支持正则表达式
driver.find_element_by_xpath("//*matchs(text(),'hao123')").click()
