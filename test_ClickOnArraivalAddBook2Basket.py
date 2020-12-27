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
def test_itemAdded2Basket():
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


def test_description():
    driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[1]/a').click()
    time.sleep(1)
    # driver.find_element_by_link_text('Description').click()
    p=driver.find_element_by_xpath('//*[@id="tab-description"]/p').text
    assert "The Selenium WebDriver Recipes book is a quick problem-solving guide to automated testing web applications with Selenium WebDriver. It contains hundreds of solutions to real-world problems, with clear explanations and ready-to-run test scripts you can use in your own projects."==p
    print("The peregraph description is OK")

def test_checkReview():#verify that there are no reviews
    reviews=driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[2]').text
    assert "REVIEWS (0)" ==reviews
    print("Test pass! there are no reviews")

def test_addingBooksMoreThanLimit():
    quantity=driver.find_element_by_css_selector('.input-text.qty.text')
    quantity.send_keys('406')
    driver.find_element_by_css_selector('.single_add_to_cart_button.button.alt').click()
    # print(quantity.get_attribute("validationMessage"))
    assert ("Value must be less than or equal to 387.")==quantity.get_attribute("validationMessage")
    print("The tooltip is fine! - Test Pass!")


def test_navToBasket():
    driver.find_element_by_css_selector('.woocommerce-message>a').click()
    title=driver.find_element_by_css_selector('.cart_totals>h2')
    wait =WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart_totals>h2'), "Basket Totals"))
    driver.back()
    driver.find_element_by_css_selector('.cartcontents').click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart_totals>h2'), "Basket Totals"))

def test_addCupon():
    driver.find_element_by_css_selector('[name="coupon_code"]').send_keys('krishnasakinala')
    time.sleep(2)
    driver.find_element_by_css_selector('[type="submit"]').click()
    final=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[2]/div/table/tbody/tr[4]/td').text
    assert "₹472.50"== final
    driver.find_element_by_css_selector('[name="coupon_code"]').send_keys('krishnasakinala')
    driver.find_element_by_css_selector('[type="submit"]').click()
    text=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/ul/li').text
    assert "Coupon code already applied!" ==text

def test_removeItem():
    removeButton=driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a')
    actions=ActionChains(driver)
    actions.move_to_element(removeButton).perform()
    assert "Remove this item"==removeButton.get_attribute('title')
    time.sleep(1)
    removeButton.click()
    wait=WebDriverWait(driver, 15)
    text=driver.find_element_by_css_selector('#page-34 > div > div.woocommerce-message')
    assert "Selenium Ruby removed. Undo?"==text.text
    time.sleep(1)


def test_updateBasket():
    driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/a').click()#click Undo button
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td/input[1]').is_enabled()==False
    print("The Update button is disabled as should be!")
    time.sleep(1)
    # area=driver.find_element_by_css_selector('.quantity>input')
    # up=driver.find_element_by_css_selector()
    # actions=ActionChains(driver)
    # actions.move_to_element(area).click().perform
    driver.find_element_by_css_selector('.input-text.qty.text').clear()
    driver.find_element_by_css_selector('.input-text.qty.text').send_keys("3")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td/input[1]').is_enabled()==True
    driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[2]/td/input[1]').click()
    total= driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[2]/div/table/tbody/tr[3]/td/strong/span').text
    assert '₹1,575.00' ==total

def test_Checkout():
    driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[2]/div/div/a').click()
    wait=WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="customer_details"]/div[1]/div/h3'), "Billing Details"))
    driver.find_element_by_css_selector('#billing_first_name').send_keys("Idan")
    driver.find_element_by_css_selector('#billing_last_name').send_keys("Bob")
    driver.find_element_by_css_selector('#billing_email').send_keys("test@gmail.com")
    driver.find_element_by_css_selector('#billing_phone').send_keys("0525666181")
    # ddl =Select(driver.find_element_by_xpath('//*[@id="billing_country"]'))
    # ddl.select_by_value("JP")
    driver.find_element_by_css_selector('#billing_address_1').send_keys('Bar Ilan')
    driver.find_element_by_css_selector('#billing_city').send_keys("BatYam")
    # ddl2=Select(By.CSS_SELECTOR, '#billing_country')
    # ddl2.select_by_value("JP")
    driver.find_element_by_css_selector('#billing_postcode').send_keys("123456")
    time.sleep(1)
    # add scrolling
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
    time.sleep(3)
    driver.find_element_by_css_selector('#payment_method_cheque').click()

    time.sleep(1)

    driver.find_element_by_css_selector('.showcoupon').send_keys('krishnasakinala')
    time.sleep(2)
    driver.find_element_by_css_selector("#place_order").click()
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/p[1]'), "Thank you. Your order has been received."))
    # time.sleep(5)
    # assert "Basket Totals" ==title.text
# def test_teardown():
#     driver.quit()