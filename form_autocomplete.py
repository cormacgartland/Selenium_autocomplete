from selenium import webdriver
import time


# webdriver initialization -- copy and paste chromedriver.exe into your workspace folder if
# you don't want it existing in your C drive (Win).
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")


# Form autocomplete start
driver.find_element_by_name("name").send_keys("Namey")
driver.find_element_by_name("email").send_keys("supernot.fakeemail@superlegit.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("password")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_id("exampleFormControlSelect1").click()
driver.find_element_by_xpath("//option[contains(text(),'Female')]").click()
driver.find_element_by_id("inlineRadio1").click()
driver.find_element_by_name("bday").send_keys("12311990")
driver.find_element_by_css_selector("input.btn").click()

# small JS automation to scroll back up to the top once form is submitted
# before naviagating to the "Shop" page
driver.execute_script("window.scrollTo(0, 0)")
time.sleep(2)

#navigation to shop page
driver.find_element_by_link_text("Shop").click()
products = driver.find_elements_by_xpath("//div[@class='card h-100']")


# loop thru product titles til the correct one is selected
for product in products:
    phone = product.find_element_by_xpath("div/h4/a").text 
    if phone == "Nokia Edge":
        product.find_element_by_xpath("div/button").click()


# navigation to checkout window
driver.find_element_by_partial_link_text("Checkout").click()
time.sleep(2)
# navigation to final page
driver.find_element_by_css_selector("button.btn-success").click()


# check terms and coditions box, search for relevant country, sleep for results,
# navigate to choose coutry, finally hit purchase and ultimately close window
driver.find_element_by_css_selector("div.checkbox-primary").click()
driver.find_element_by_css_selector("input.validate").send_keys("United")
time.sleep(5)
driver.find_element_by_link_text("United States of America").click()
driver.find_element_by_css_selector("input.btn-success").click()


# close window
time.sleep(2)
driver.close()