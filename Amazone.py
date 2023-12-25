from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options= Options ()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
#search_box= driver.find_element(By.)