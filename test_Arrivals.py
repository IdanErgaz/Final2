
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest, time
########################################################################

def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://practice.automationtesting.in/")
    driver.implicitly_wait(10)

def test_checkArrivels():
    driver.find_element_by_id("menu-item-40").click()
    driver.find_element_by_link_text("Home").click()
    arraivalElement=driver.find_elements_by_css_selector('.themify_builder_sub_row.clearfix.gutter-default.sub_row_1-0-2 >div')
    print(len(arraivalElement))
    assert 3==(len(arraivalElement))
    print("Test Pass!!!")
def test_teardown():
    driver.quit()