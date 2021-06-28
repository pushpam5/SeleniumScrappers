from selenium import webdriver
import time
import csv
import re

FILE_NAME = f'file_path'

with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['Name','Website','Address','Phone_No','Email','Details']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()


DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.mnhandsandvoices.org/resources-information/resource-directory/national-organizations'
driver.get(url)
time.sleep(3)
divisions = driver.find_elements_by_class_name('bios_expand_one')
for j in divisions:
    obj = {}
    link = j.find_element_by_tag_name('a')
    print(link.text)
    obj['Name'] = link.text
    link.click()
    time.sleep(2)
    ele = j.find_element_by_class_name('long_description')
    para = ele.find_elements_by_tag_name('p')
    try:
        print(para[0].find_element_by_tag_name('a').get_attribute('href'))
        obj['Website'] = para[0].find_element_by_tag_name('a').get_attribute('href')
    except:
        obj['Website'] = '-'
    try:
        print(para[1].text)
        obj['Address'] = para[1].text
    except:
        print("error")
        obj['Address'] = '-'
    try:
        print(para[2].text)
        obj['Phone_No'] = para[2].find_element_by_tag_name('a').get_attribute('href')
    except:
        obj['Phone_No'] = '-'
    try:
        print(para[3].find_element_by_tag_name('a').get_attribute('href'))
        obj['Email'] = para[3].find_element_by_tag_name('a').get_attribute('href')
    except:
        obj['Email'] = '-'
    try:
        print(ele.text)
        obj['Details'] = str(ele.text).split('\n')
    except:
        obj['Details'] = '-'
        print("error")
    with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writerow(obj)
    print(obj)