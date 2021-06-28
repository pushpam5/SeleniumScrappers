from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = f'file_path'
DRIVER_PATH = 'driver_path'



with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.earthday.org/')
links = []
val =driver.find_elements_by_class_name('logo')
for i in val:
    try:
        a = i.find_element_by_tag_name('a')
        print(a.get_attribute('href'))
        links.append(a.get_attribute('href'))
    except:
        print("Error")
save(links)