from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://duckduckgo.com/?q=")

driver.maximize_window()
time.sleep(10)

ele = driver.find_element(By.ID,"searchbox_input")
ele.send_keys("stockwiz")

time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'lxml')
links = soup.find_all('a', class_='eVNpHGjtxRBq_gLOfGDr LQNqh2U1kzYxREs65IJu')
for link in links:
    print( link.get_text(strip=True))


