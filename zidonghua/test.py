from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

edge_path = 'D:\python\msedgedriver.exe'
s = Service(edge_path)
driver = webdriver.Edge(service=s)
driver.get(url="https://www.baidu.com")

try:
    elements = driver.find_elements(By.XPATH, "//*[contains(text(),boss)]")
    for element in elements:
        print(element)
except NoSuchElementException:
    print("11")

driver.quit()
