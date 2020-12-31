import pytest, time, unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
@pytest.yield_fixture()
def setUp():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get('http://practice.automationtesting.in/')

    yield
    print("Finish the test!")
    driver.quit()


def test_registrationWithInvalidEmail(setUp):
    driver.find_element(By.XPATH, '//*[@id="menu-item-50"]/a').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_login"]/div[2]/h2'), "Register"))#Wait for register title
    driver.find_element(By.ID, 'reg_email').send_keys('greek07')
    time.sleep(2)
    driver.find_element(By.ID, 'reg_password').clear()
    driver.find_element(By.ID, 'reg_password').send_keys('ZibZab55443322')
    driver.find_element(By.ID, 'reg_password').send_keys(Keys.ENTER)
    time.sleep(2)
    # wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.strong'), 'Strong'))

    # driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()

    # driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').send_keys(Keys.ENTER)

    # driver.find_element(By.ID, 'reg_email').get_attribute()
    email=driver.find_element_by_id('reg_email')
    # print(email.get_attribute("validationMessage"))

    assert ("Please include an '@' in the email address. 'greek07' is missing an '@'.")==email.get_attribute("validationMessage")

def test_registerWithEmptyEmail(setUp):
    driver.find_element(By.XPATH, '//*[@id="menu-item-50"]/a').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_login"]/div[2]/h2'), "Register"))
    # driver.find_element(By.ID, 'reg_email').send_keys('greek07')
    # time.sleep(2)
    driver.find_element(By.ID, 'reg_email').clear()
    driver.find_element(By.ID, 'reg_password').clear()
    driver.find_element(By.ID, 'reg_password').send_keys('ZibZab55443322')
    time.sleep(1)
    driver.find_element(By.ID, 'reg_password').send_keys(Keys.SPACE)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.strong'), 'Strong'))

    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()

    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').send_keys(Keys.SPACE)
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-36"]/div/div[1]/ul/li'), 'Error: Please provide a valid email address.'))
    title=driver.find_element_by_css_selector('#page-36 > div > div.woocommerce > ul > li').text
    print(title)
    assert  title=="Error: Please provide a valid email address."

    # assert ("Please include an '@' in the email address. 'greek07' is missing an '@'.") == email.get_attribute("validationMessage")

def test_registerWithoutPassword(setUp):
    driver.find_element(By.XPATH, '//*[@id="menu-item-50"]/a').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_login"]/div[2]/h2'), "Register"))
    driver.find_element(By.ID, 'reg_email').send_keys('greek007@walla.com')
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-36"]/div/div[1]/ul/li'),'Error: Please enter an account password.'))
    title = driver.find_element_by_css_selector('#page-36 > div > div.woocommerce > ul > li').text
    print(title)
    assert title == "Error: Please enter an account password."


