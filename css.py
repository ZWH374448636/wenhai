from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

#css通过id属性定位
driver.find_element_by_css_selector("#kw").send_keys("python")

#css通过标签和id属性组合定位
driver.find_element_by_css_selector("input#kw").send_keys("python")

#css通过class属性定位
driver.find_element_by_css_selector(".s_ipt").send_keys("python")

#css通过标签和class属性的组合定位
driver.find_element_by_css_selector("input.s_ipt").send_keys("python")

#css通过name属性定位
driver.find_element_by_css_selector("[name='wd']").send_keys("python")

#css通过标签和其它属性组合定位
driver.find_element_by_css_selector("input[id='kw']").send_keys("python")

#css通过层级关系定位
driver.find_element_by_css_selector("input#form>span>input").send_keys("python")

#css通过索引方式定位
driver.find_element_by_css_selector("select#nr>option:nth-child(1)")

#css通过逻辑运算定位
driver.find_element_by_css_selector("input[id='kw'][name='wd']").send_keys("python")
