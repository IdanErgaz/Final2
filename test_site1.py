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
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="C:/Projects/Automation/Drivers/chromedriver.exe")
    driver.maximize_window()
    driver.get("http://demo.automationtesting.in/Index.html")
#
# def test_BadSignIn():
#     driver.find_element(By.ID, "btn1").click()
#     driver.find_element(By.CSS_SELECTOR, '[placeholder="E mail"]').send_keys("pop3@walla.com")
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '[placeholder="Password"]').send_keys("123456")
#     driver.find_element(By.ID, "enterbtn").click()
#     wait=WebDriverWait(driver,10)
#     errorText=driver.find_element(By.CSS_SELECTOR, '[ng-show="showerror"] >label').text
#     print("Idan:", errorText)
#     wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[ng-show="showerror"] >label'),"Invalid User Name or PassWord" ))
#
# def test_register():
#     driver.back()
#     driver.find_element(By.ID, "btn2").click()#click on skip sign in button
#     time.sleep(1)
#     driver.find_element(By.CSS_SELECTOR, '[placeholder="First Name"]').send_keys("_Arrwa") #name
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[1]/div[2]/input').send_keys("Asrrd4sw1")#LastName
#     time.sleep(2)
#     driver.find_element_by_xpath('//*[@id="eid"]/input').send_keys("www2@gmail.com")#Email
#     time.sleep(3)
#     driver.find_element_by_xpath('/html/body/section/div/div/div[2]/form/div[4]/div/input')
#     time.sleep(1)
#     driver.find_element_by_css_selector('[value="Male"]').click() #gender
#     time.sleep(1)
#     driver.find_element_by_id('checkbox2').click() #select movies checkbox
#     time.sleep(1)
#     driver.find_element(By.ID, "msdd").click()
#     driver.find_element(By.XPATH, '//*[@id="basicBootstrapForm"]/div[7]/div/multi-select/div[2]/ul/li[5]/a').click()#select Czech
#     time.sleep(1)
#     driver.find_element(By.ID, "imagesrc").send_keys("E:/TestFiles/image1.png")
#     time.sleep(1)
#     skils = Select(driver.find_element_by_id("Skills"))
#     skils.select_by_value("SQL")
#     time.sleep(1)
#     country=Select(driver.find_element_by_id("countries"))
#     country.select_by_value("Israel")
#     time.sleep(1)
#     driver.find_element_by_id("firstpassword").send_keys("Zubur123")
#     time.sleep(1)
#     driver.find_element_by_id("secondpassword").send_keys("Zubur123")
#     time.sleep(2)
#     driver.find_element(By.ID, "submitbtn").click()
#     ########################
#     phone = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#basicBootstrapForm > div:nth-child(4) > div > input")))
#     print(phone.get_attribute("validationMessage"))
#     assert ("Please fill out this field.")==phone.get_attribute("validationMessage")
#     driver.find_element(By.CSS_SELECTOR, "#basicBootstrapForm > div:nth-child(4) > div > input").send_keys("0553444171")
#     time.sleep(2)
#     yearBox=Select(driver.find_element_by_id("yearbox")) #set year ddl
#     yearBox.select_by_value("1980")#select from the year ddl
#     monthBox=Select(driver.find_element_by_xpath('//*[@id="basicBootstrapForm"]/div[11]/div[2]/select'))
#     monthBox.select_by_value("September")
#     dayBox=Select(driver.find_element(By.ID, "daybox"))
#     dayBox.select_by_value("30")
#     driver.find_element(By.ID, "submitbtn").click()
#     titleh4=driver.find_element_by_tag_name
#     wait=WebDriverWait(driver, 10)
#     wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'body > section > div:nth-child(1) > div > div:nth-child(2) > h4:nth-child(1)'),"- Double Click on Edit Icon to EDIT the Table Row." ))
#     time.sleep(4)
#     button=driver.find_element_by_css_selector('.btn.btn-xs.btn-custom')
#     print("Is displayed:", button.is_displayed())
#     actions=ActionChains(driver)
#     actions.double_click(button).perform()
#     time.sleep(2)
#     driver.find_element_by_tag_name('cancel-click').click()
#     # element=wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#\31 608816340224-0-uiGrid-000B-cell > user-click-select > div:nth-child(2) > cancel-click > button"))
#
#
#     print("Cancel button can be seen !!!")
#     # errorMessage = driver.find_element(By.id("email")).getAttribute("validationMessage")
#     # print(errorMessage)
#     # field_name = models.Field(error_messages={"key": "message"})


# def test_Alerts():
#     driver.get("http://demo.automationtesting.in/WebTable.html")
#     time.sleep(2)
#     switch2=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
#     alerts=driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[1]/a')
#     actions=ActionChains(driver)
#     actions.move_to_element(switch2).click(alerts).perform()#enter to the Alerts section
#     time.sleep(5)
#     driver.find_element(By.XPATH,'// *[ @ id = "OKTab"] / button').click()
#     assert(driver.switch_to_alert().text)=="I am an alert box!"
# def test_skipSignIn():
#     driver.find_element(By.ID, "btn2").click() #click on skip sign in button

def test_AutoComplete():
    #nav to register and start typing and check options
    driver.get("http://demo.automationtesting.in/WebTable.html")

    widgets=driver.find_element_by_xpath('//*[@id="header"]/nav/div/div[2]/ul/li[5]/a')
    AutoComplete= driver.find_element_by_xpath('//*[@id="header"]/nav/div/div[2]/ul/li[5]/ul/li[2]/a')
    actions= ActionChains(driver)
    actions.move_to_element(widgets).click(AutoComplete).perform()
    time.sleep(10)
    # driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/div[1]/div').send_keys("test")
    driver.find_element_by_xpath('/html/body/section/div[1]/div[2]/div[1]/span').send_keys("test")
#
# def test_teardown():
#     driver.quit()