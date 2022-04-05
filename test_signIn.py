from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

@pytest.fixture
def setUp():
    global driver,name,dob,address,pincode,phno,email,password,password1
    name = input("Enter name")
    dob = input("Enter date of birth")
    address = input("Enter the address")
    pincode = int(input("Enter the pincode"))
    phno = int(input("Enter phone number"))
    email = input("Enter the email-id")
    password = input("Enter the password")
    password1 = input("Enter the password again to confirm")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

@pytest.fixture
def assign():
    global driver,email,password
    email = input("Enter email:")
    password = input("Enter the password:")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.close()

def test_signin(assign):
    driver.get("https://iprimedtraining.herokuapp.com/training.php")
    driver.find_element_by_name("loginEmail").send_keys(email)
    time.sleep(1)
    driver.find_element_by_name("loginpass").send_keys(password)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[1]/form/table/tbody/tr[3]/td[2]/button").click()

def test_signupNew(setUp):
    driver.get("https://iprimedtraining.herokuapp.com/training.php")
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input[1]").click()
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[3]/td[2]/select/option[3]").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[4]/td[2]/input").send_keys(dob)
    driver.find_element_by_name("Address").send_keys(address)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/input").send_keys(pincode)
    time.sleep(1)
    driver.find_element_by_name("Mobile").send_keys(phno)
    driver.find_element_by_name("Email").send_keys(email)
    driver.find_element_by_name("pass").send_keys(password)
    driver.find_element_by_name("cnfpass").send_keys(password1)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[11]/td[2]/div/input").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element_by_name("subbtn").click()
    time.sleep(3)
