from selenium import webdriver
import time
import csv
import re


FILE_NAME = f'file_path'
DRIVER_PATH = 'driver_path'



with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['name','link','website','address','Phone','Email']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()



driver = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://www.edf-feph.org/our-members/'
driver.get(url)
time.sleep(3)
ele = driver.find_elements_by_class_name('m_panel__content')
names = []
links = []
for i in ele:
    link = i.find_element_by_tag_name('a')
    print(link.text)
    names.append(link.text)
    links.append(link.get_attribute('href'))
    print(link.get_attribute('href'))
length = len(names)
print(length)
for i in range(length):
    obj = {}
    obj['name'] = names[i]
    obj['link'] = links[i]

    driver.get(links[i])
    time.sleep(2)

    try:
        div = driver.find_element_by_class_name('m_hero__content')
        a = div.find_element_by_tag_name('a')
        print(a.get_attribute('href'))
        obj['website'] = a.get_attribute('href')
    except:
        obj['website'] = '-'
    try:
        address = driver.find_element_by_class_name('text--address')
        obj['address'] = address.text
        print(address.text)
    except:
        obj['address'] = '-'
    try:
        phone = driver.find_element_by_class_name('text--phone')
        obj['Phone'] = phone.text
        print(phone.text)
    except:
        obj['Phone'] = '-'
    try:
        email = driver.find_element_by_class_name('text--mail')
        obj['Email'] = email.text
        print(email.text)
    except:
        obj['Email'] = '-'
    with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=fields)
        writer.writerow(obj)
    print(obj)
