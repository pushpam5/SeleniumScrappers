from selenium import webdriver
import time
import csv
import re

FILE_NAME = f'file_path'

with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['Name','Link','address','details','websites']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()


DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# url path
driver.get('https://www.charitychoice.co.uk/charities/human-rights/lesbian-gay-bisexual-and-transgender')
time.sleep(3)
name = []
links = []
while True:
    try:
        charities = driver.find_elements_by_class_name('charity-search-rows')
        for ele in charities:
            heading = ele.find_element_by_tag_name('h2')
            link = heading.find_element_by_tag_name('a')
            print(link.text)
            print(link.get_attribute('href'))
            name.append(link.text)
            links.append(link.get_attribute('href'))
        print(len(name))
        print(len(links))
        button = driver.find_element_by_class_name('pager__item--next')
        button.click()
        time.sleep(3)

    except Exception as e:
        print(e)
        break
print(links)
print(name)
length = len(links)
for i in range(length):
    obj = {}
    driver.get(links[i])
    time.sleep(1)
    obj['Name'] = name[i]
    obj['Link'] = links[i]
    try:
        cont = driver.find_element_by_class_name('inner-column')
        container = cont.find_element_by_class_name('container')
        rows = container.find_elements_by_class_name('row')
        try:
            address = rows[0].find_element_by_class_name('col-5')
            print(address.text)
            obj['address'] = address.text
        except:
            obj['address'] = '-'
        try:
            details = rows[0].find_element_by_class_name('col-7')

            print(details.text)
            obj['details'] = str(details.text).split('\n')
        except:
            obj['details'] = '-'
        try:
            web = rows[1].text
            print(web)
            obj['websites'] = str(web).split('\n')
        except:
            obj['websites'] = '-'
        print(obj)
        with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writerow(obj)
    except:
        print("error")