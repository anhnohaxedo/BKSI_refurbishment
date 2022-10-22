from msilib.schema import tables
from xml.dom.minidom import Element
from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import re

driver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())
driver.get('http://dkhp.itc.edu.vn/QuyChe43.aspx')
tables = driver.find_elements(By.CSS_SELECTOR, 'table')
file = open('D:/project/BKSI/BKSI_refurbishment/scrapping/regulation/itc' + '.txt', 'w', newline='', encoding='utf-8')
for table in tables:
    elements = table.find_elements(By.CSS_SELECTOR, 'p')
    #chưa chia điều khoản
    for element in elements:
        file.write(element.text)
        file.write('\n')
file.close()
driver.quit()

