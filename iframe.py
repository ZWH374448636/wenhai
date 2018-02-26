from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.126.com/")
driver.implicitly_wait(10)
ifr = driver.find_element_by_id("x-URS-iframe")
driver.switch_to.frame(ifr)
driver.find_element_by_name("email").send_keys("zwh2537")
driver.find_element_by_name("password").send_keys("ABC19891969")
driver.switch_to.default_content()
