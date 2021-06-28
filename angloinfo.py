from selenium import webdriver
import time
import csv

FILE_NAME = f'file_path'

with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['name', 'description','website','Contact_No']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()

DRIVER_PATH = 'driver-path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://www.angloinfo.com/seoul/directory/seoul-charities-ngos-voluntary-work-548'
driver.get(url)
time.sleep(4)
names = driver.find_elements_by_class_name('item-name')
description = driver.find_elements_by_class_name('item-description')
contact = driver.find_elements_by_class_name('contact-panel')

print(len(names),len(description),len(contact))
i = 0
while i < len(names):
    obj = {}
    obj['name'] = names[i].text
    print(obj['name'])
    obj['description'] = description[i].text
    print(obj['description'])
    print(contact[i].text)
    try:
        li = contact[i].find_element_by_tag_name('li')
        a = li.find_element_by_tag_name('a')
        print(a.get_attribute('href'))
        obj['website'] = a.get_attribute('href')
    except:
        obj['website'] = '-'
    try:
        cli = contact[i].find_element_by_class_name('show-number')
        cli.click()
        time.sleep(1)
        contact_number = contact[i].find_element_by_class_name('hidden-phone')
        print(contact_number.text)
        obj['Contact_No'] = contact_number.text
    except:
        obj['Contact_No'] = '-'
    print(obj)
    with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writerow(obj)
    i += 1
