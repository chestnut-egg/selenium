import os
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome("/home/ppg/PycharmProjects/AutoTest/driver/chromedriver")
# driver.get("https://www.baidu.com/")

# input_first = driver.find_element_by_xpath('//*[@id="u1"]/a[7]')
# input_first.click()

# input_css = driver.find_element_by_css_selector('#u1 > a.lb')
# input_css.click()
#
# find_re = driver.find_element(By.CSS_SELECTOR,"#u1 > a.lb")

global driver


def ready(this_driver):
    global driver
    driver = this_driver

def click(xpath):
    click = driver.find_element_by_xpath(xpath)
    click.click()

def click_by_css(css):
    click = driver.find_element_by_css_selector(css)
    click.click()
