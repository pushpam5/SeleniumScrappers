from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = 'file-path'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
pause_time = 4
DRIVER_PATH = 'file-path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://arab.org/directory?wpbdp_view=all_listings')
while True:
    div = driver.find_elements_by_class_name('listing-title')
    div_det = driver.find_elements_by_class_name('excerpt-content')
    for i in range(len(div)):
        key = {}
        try:
            a = div[i].find_element_by_tag_name('a')
            print(a.text)
            print(a.get_attribute('href'))
            key['organisation_name'] = a.text
            key['organisation_link'] = a.get_attribute('href')
        except:
            key['organisation_name'] = "-"
            key['organisation_link'] = "-"
        try:
            a = div_det[i].find_element_by_class_name('listing-details')
            vals = a.find_elements_by_class_name('field-label')
            valb = a.find_elements_by_class_name('value')
            for j in range(len(vals)):
                print(vals[j].text)
                print(valb[j].text)
                key[vals[j].text] = valb[j].text
        except Exception as e:
            print(e)
        with open(FILE_NAME) as file:
            data = json.load(file)
            data.append(key)
            save(data)
        print(key)
    try:
        button = driver.find_element_by_class_name('next')
        button.click()
        time.sleep(pause_time)
    except:
        break