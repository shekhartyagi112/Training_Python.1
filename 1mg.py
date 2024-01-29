from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.selenium_manager import SeleniumManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

options = Options()
options.add_experimental_option("detach",True)
driver= webdriver.Chrome(options = options)   #executable_path="D:\drivers\chromedriver.exe", chrome_options=chrome_options)

driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.1mg.com/")
time.sleep(2)
driver.find_element(By.XPATH,"//*[name()='path' and contains(@fill,'#ffffff')]").click()

driver.find_element(By.XPATH,"//*[@id='srchBarShwInfo']").send_keys("whey")
time.sleep(1)
#driver.find_element(By.XPATH,"(//div[@class='styles__name___-ixKa'])[1]").click()
#time.sleep(3)