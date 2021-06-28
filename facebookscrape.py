from selenium import webdriver
import time
import csv
import json
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select


FILE_NAME = f'file_path'
DRIVER_PATH = 'driver_path'



with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['name', 'link','details']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()



driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
url = 'https://www.facebook.com/places/Charity-Organization-in-Vienna-Austria/111165112241092/226326230802065/'
driver.get(url)
time.sleep(5)
count = 0
names = []
while count < 50:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    print(count)
    count += 1
ele = driver.find_elements_by_class_name('_6v55')
links = []
for i in ele:
    try:
        li = i.find_element_by_tag_name('a')
        print(li.text,li.get_attribute('href'))
        links.append(li.get_attribute('href'))
        names.append(li.text)
    except:
        continue
print(links)
print(names)
for j in range(len(names)):
    obj = {}
    obj['name'] = names[j]
    obj['link'] = links[j]
    driver.get(links[j])
    time.sleep(1)
    try:
        l = driver.find_element_by_class_name('_u9q')
        obj['details'] = str(l.text).split('\n')
        print(l.text)
    except:
        obj['details'] = '-'
    with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writerow(obj)