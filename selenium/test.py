from selenium import webdriver
from utils import api

driver = webdriver.Chrome("/home/ppg/PycharmProjects/selenium/driver/chromedriver")
driver.get("https://www.baidu.com/")

api.ready(driver)

api.click('//*[@id="u1"]/a[7]')