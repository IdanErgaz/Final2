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
    list=driver.find_element_by_xpath('//*[@id="n2-ss-6"]')
    print(list)

def test_Validate3Sliders():
    element=driver.find_elements_by_css_selector('.n2-ss-slide-background-image.n2-ss-slide-fill.n2-ow')
    assert 3==(len(element)), "test failed!!!"
    print("There are only 3 elements in the carousel")
    print("Test Pass")

def test_teardown():
    driver.quit()
# To Get the Number of Items in the Carousel
#
# String selector = “li[class^=a-carousel-card]”;
#
# ArrayList items = driver.findElements(By.cssSelector(selector));
#
# ArrayList<String> list1 = new ArrayList<String>();
#
# String name;
#
# <div style=”clear:both; margin-top:0em; margin-bottom:1em;”><a href=”http://www.testingexcellence.com/how-to-upload-files-using-selenium-and-autoit/” target=”_blank” rel=”nofollow” class=”u5f66b656a489f77a84dd8f1a1d2f8cfb”><div style=”padding-left:1em; padding-right:1em;”><span class=”ctaText”></span>  <span class=”postTitle”>How to Upload and Submit Files Using Selenium and AutoIt</span></div></a></div>
#
# for(int i=0; i<items; i++) {
#
# int index = i+1;
# ArrayList items = driver.findElements(By.cssSelector(selector));

