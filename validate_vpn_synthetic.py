from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time

# start web browser
options = Options()
options.add_argument('--headless')
driver=webdriver.Chrome("/home/ubuntu/chromedriver", chrome_options=options)

# get source code
driver.get("http://boutique-shop-2090566869.us-west-1.elb.amazonaws.com/")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(2) .hot-product-card-img-overlay").click()
driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-3:nth-child(3) img").click()
driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary").click()
driver.find_element(By.CSS_SELECTOR, ".cymbal-button-primary:nth-child(1)").click()
html = driver.page_source

print(html)

driver.close()
driver.quit()
