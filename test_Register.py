import pytest, time, unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get('http://practice.automationtesting.in/')

def test_register():
    driver.find_element(By.XPATH, '//*[@id="menu-item-50"]/a').click()
    wait=WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_login"]/div[2]/h2'), "Register"))
    driver.find_element(By.ID, 'reg_email').send_keys('greek07@walla.com')
    driver.find_element(By.ID, 'reg_password').send_keys('Zubur123Zubur')
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.strong'), 'Strong'))
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').send_keys(Keys.ENTER)
    # driver.find_element(By.CSS_SELECTOR, '.woocommerce-Button.button').click()
    time.sleep(3)
    title=driver.find_element(By.XPATH, '//*[@id="page-36"]/div/div[1]/div/p[1]').text
    print("Title:", title)
    assert title=="Hello greek07 (not greek07? Sign out)"

def test_signoutAnLogInWith():
    driver.find_element(By.LINK_TEXT, 'Sign out').click()  #click on sign out link
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_login"]/div[2]/h2'), "Register"))
    driver.find_element(By.ID, 'reg_email').send_keys('greek07@walla.com')
    driver.find_element(By.ID, 'reg_password').send_keys('Zubur123Zubur')
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.strong'), 'Strong'))
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').send_keys(Keys.ENTER)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-36"]/div/div[1]/ul/li'), 'Error: An account is already registered with your email address. Please login.'))
    title=driver.find_element(By.XPATH, '//*[@id="page-36"]/div/div[1]/ul/li').text
    assert "Error: An account is already registered with your email address. Please login."==title


def test_teardown():
    print("Finish Testing!")
    driver.quit()