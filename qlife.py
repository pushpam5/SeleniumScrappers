from selenium import webdriver
import time
import csv
import re

FILE_NAME = f'file_path'

with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['Name','Link','Details']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()

DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://qlife.org.au/resources/directory')
time.sleep(3)

sect = driver.find_elements_by_tag_name('section')
for i in sect[1:11]:
    print(i.get_attribute('id'))
    try:
        ele = i.find_element_by_class_name('text-block')
        para = ele.find_elements_by_tag_name('p')
        for j in para:
            obj = {}
            try:
                a = j.find_element_by_tag_name('a')
                print(a.get_attribute('href'))
                obj['Name'] = a.text
                obj['Link'] = a.get_attribute('href')
                obj['Details'] = j.text
                print(obj)
                with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
                    writer = csv.DictWriter(csvFile, fieldnames=fields)
                    writer.writerow(obj)
            except:
                print(j.text)
    except:
        print("Error")