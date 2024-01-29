import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
#Opetion is use for stop the chrome page after complete script, it will not close automatically.

options = Options()
options.add_experimental_option("detach",True)

#Webdriver.Chrome is for launch the chrome browser.

driver = webdriver.Chrome(options = options)

#driver.maximize_window is for maximize the browser page.

driver.maximize_window()

#driver.get is for launch & navegate the site Url.

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#implicity_wait is use for given the time for load the perticular browser or navegation page successfully.

driver.implicitly_wait(5)
#driver.find_element(By.ID,"checkBoxOption1").click()    #Click on Check-Box
time.sleep(2)
#driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()  #click on link
time.sleep(2)

#it is for select the radio button.

driver.find_element(By.CSS_SELECTOR,"input[value='radio1']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[value=radio2]").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"input.radioButton[value=radio3]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//*[@value='radio2' and @name='radioButton']").click()

#it is use for enter the text or value.
Name= driver.find_element(By.XPATH,"//*[@id='name']")
Name.send_keys("Shekhar")

#it is use for clear the text or value from text box.
Name.clear()
Name.send_keys(" Shekhar Tyagi")

Alert= driver.find_element(By.XPATH,"//legend[normalize-space()='Switch To Alert Example']")
Alert1= Alert.text
print(Alert1)

#it is use for select the multi check-Box with for loop condition.

check_boxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for check_box in check_boxes:
    if check_boxes.index(check_box)+1 !=2:
        check_box.click()
print(check_boxes)
print(len(check_boxes))
time.sleep(1)

#it is use for select the value from dropdown list. 3 mathods is used for select the dropdown value.

static_dropdown= driver.find_element(By.ID,"dropdown-class-example")
select=Select(static_dropdown)
select.select_by_index(2)
time.sleep(2)
select.select_by_value("option1")
time.sleep(2)
select.select_by_visible_text("Option3")
time.sleep(2)

#it is use for direct selection from dropdown list.

drop= driver.find_element(By.XPATH,"//option[@value='option2']").click()

#get attribute mathod is use for get the anu url from website.

links= driver.find_element(By.CLASS_NAME,"blinkingText")
print(links.get_attribute("href"))








