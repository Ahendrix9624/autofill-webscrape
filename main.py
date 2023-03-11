"""
USAGE - The code uses the Selenium WebDriver to automate filling out a Google Form and submitting it.

        It reads data from a JSON file and inputs the values of "first_name" and "last_name" in the form. 
        Then it selects a radio button and clicks the "submit" button.

        After that, the code waits for a confirmation message, reads the message from the page, 
        and checks if the message is "Thank you for attending". Based on the result, it prints 
        a message whether the test was successful or not.
        
AUTHOR - https://github.com/Ahendrix9624/
"""
from selenium import webdriver
import time
import json

with open('data.json', 'r') as data_file:
    data = json.load(data_file)

driver = webdriver.Chrome()
driver.get('https://forms.gle/UAtyz22qMFY8jazcA')

time.sleep(2)

LastName = data['last_name']
last = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
last.send_keys(LastName)

FirstName = data['first_name']
first = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
first.send_keys(FirstName)

RadioButtonPeriod = driver.find_element("xpath",'//*[@id="i22"]/div[3]/div')
RadioButtonPeriod.click()

Submit = driver.find_element("xpath",'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
Submit.click()

get_confirmation_div_text = driver.find_element_by_css_selector('vHW8K')
print(get_confirmation_div_text.text)
if ((get_confirmation_div_text.text) == "Thank you for attending"):
    print ("Test Was Successful")
else:
    print("Test Was Not Successful")
