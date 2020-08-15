from selenium import webdriver # 导入webdriver包
import time
driver = webdriver.Chrome()

driver.maximize_window() # 最大化浏览器 


driver.get("https://twww.lizihang.com/") # 通过get()方法，打开一个url站点


ershoufang = driver.find_element_by_css_selector("[autoid='auto_20qlf3di']")

ershoufang.click()
print("---点击二手房 频道----")
