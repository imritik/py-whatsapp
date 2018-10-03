from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('/usr/bin/chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)

target = input("Enter your friends name or group name (case sensitive)")    #friends name

# =====your own message ======

string  = input("Enter your message to be sent!!")

count = int(input("No of times msg to be sent"))

x_arg = '//span[contains(@title,'+ target + ')]'

group_title = wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
print group_title
print "after wait"
group_title.click()
inp = "//div[@contenteditable='true']"
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

input_box=wait.until(EC.presence_of_element_located((By.XPATH,inp)))

for i in range(count):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)