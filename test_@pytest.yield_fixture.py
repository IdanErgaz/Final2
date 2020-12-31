from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time, pytest, unittest
##################################################################
@pytest.yield_fixture()
def setUp():
    print("before EACH method")
    yield
    print("Print AFTER each test")
def test_login(setUp):
    print("Test login...")

def test_logout(setUp):
    print("test logout...")


