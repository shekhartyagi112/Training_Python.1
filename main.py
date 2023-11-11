from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
#this example is for link test print.
time.sleep(1)
link_banners= driver.find_elements(By.XPATH,"//div[@data-clone='false']//a")
print(f"deals: {len(link_banners)}")
#for link_banner in link_banners:
    #print(link_banner.get_attribute("href"))
    #print(link_banner.get_attribute("innerHTML"))
    #print(link_banner.get_attribute("outerHTML"))
  #it is use for stop the  multiple link command.
    #break
driver.find_elements()