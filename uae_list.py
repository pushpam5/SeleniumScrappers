from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = 'file_path'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
pause_time = 4
DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://services.iacad.gov.ae/SmartPortal/en/CharityOrganizations/Index')
sel = Select(driver.find_element_by_name('dt1_length'))
sel.select_by_value('100')
table = driver.find_element_by_id('dt1')
tbody  = table.find_element_by_tag_name('tbody')
tr = tbody.find_elements_by_tag_name('tr')
for i in tr:
    key = {}
    td = i.find_elements_by_tag_name('td')
    key['name'] = td[1].text
    key['email'] = td[2].text
    key['phone_number'] = td[3].text
    key['location'] = td[4].text
    key['address'] = td[5].text
    with open(FILE_NAME) as file:
        data = json.load(file)
        data.append(key)
        save(data)
    print(key)

