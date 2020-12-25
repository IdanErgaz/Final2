from django.forms import models
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest, time
from django.core import validators
########################################################################

driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.implicitly_wait(10)

driver.find_element_by_id("menu-item-40").click()
driver.find_element_by_link_text("Home").click()
arraivalElement=driver.find_elements_by_css_selector('.themify_builder_sub_row.clearfix.gutter-default.sub_row_1-0-2 >div')
print(len(arraivalElement))
assert 3==(len(arraivalElement))
print("Test Pass!!! there are Only 3 arraival as expected")
driver.find_element_by_xpath('//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[1]/img').click()
# button=driver.find_element_by_css_selector('#product-160 > div.summary.entry-summary > form > button')
wait=WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#product-160 > div.summary.entry-summary > form > button'))).click()
print(driver.find_element_by_css_selector('.wpmenucart-contents').text)
assert(driver.find_element_by_css_selector('.wpmenucart-contents').text)=='1 Item₹500.00'
driver.quit()