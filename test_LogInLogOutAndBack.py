from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, pytest, unittest
##################################################################

def test_setup():
    print("Opening the App")
    global driver
    driver=webdriver.Firefox(executable_path="C:/Projects/Automation/Drivers/geckodriver.exe")
    driver.maximize_window()
    driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
    driver.implicitly_wait(9)

def test_login():
    print("Start login Test...")
    driver.find_element_by_id('txtUsername').send_keys('Admin')
    driver.find_element_by_id('txtPassword').send_keys('admin123')
    driver.find_element_by_id('btnLogin').click()
    wait=WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, "//h1[contains(text(),'Dashboard')]"), 'Dashboard'))
    title=driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/h1').text
    assert 'Dashboard'==title

def test_Logout():
    print("test logout...")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="welcome"]').click()
    time.sleep(1)
    wait=WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout')))
    driver.find_element(By.LINK_TEXT, 'Logout').click()#click on ogout link

    # driver.find_element_by_link_text('Logout').click()
    time.sleep(4)
    driver.back()
    wait=WebDriverWait(driver, 15)
    # wait.until(EC.invisibility_of_element((By.XPATH, "//h1[contains(text(),'Dashboard')]")))
    dashboardTitle=driver.find_element_by_xpath('/html[1]/body[1]/div[1]/div[3]/div[1]/div[1]/h1[1]')
    print(dashboardTitle.text)
    if (dashboardTitle):
        print("Test FAIL!!!")
    print("Dashboard page can NOT be seen!!!!")
    assert dashboardTitle.text !='Dashboard'

def test_teardown():
    print("Closing app")
    # time.sleep(10)
    driver.quit()