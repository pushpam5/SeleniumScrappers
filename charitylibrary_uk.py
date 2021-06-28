from selenium import webdriver
import time
import csv
import re

FILE_NAME = f'file_path'


with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['Name','charity_No','website','Contact_Person','Phone','Address']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()


DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

count = 0
while count < 1745:
    if count == 0:
        url = 'https://www.charitylibrary.uk.com/all-charities'
    else:
        url = f'https://www.charitylibrary.uk.com/all-charities/{count}'
    count += 8
    driver.get(url)
    time.sleep(3)
    elements = driver.find_elements_by_class_name('charitiesBlock')
    for ele in elements:
        obj = {}
        try:
            print(ele.find_element_by_class_name('charityTitle').text)
            obj['Name'] = ele.find_element_by_class_name('charityTitle').text
        except:
            obj['Name'] = '-'
        try:
            classes = ele.find_elements_by_class_name('charityItem')
            try:
                try:
                    print(classes[0].text)
                    obj['charity_No'] = classes[0].text
                except:
                    obj['charity_No'] = '-'
                try:
                    print(classes[1].find_element_by_tag_name('a').get_attribute('href'))
                    obj['website'] = classes[1].find_element_by_tag_name('a').get_attribute('href')
                except:
                    obj['website'] = '-'
                try:
                    print(classes[2].text)
                    obj['Contact_Person'] = classes[2].text
                except:
                    obj['Contact_Person'] = '-'
                try:
                    print(classes[3].text)
                    obj['Phone'] = classes[3].text
                except:
                    obj['Phone'] = '-'
                try:
                    print(classes[6].text)
                    obj['Address'] = classes[6].text
                except:
                    obj['Address'] = '-'
            except:
                print("error")
            print(obj)
            with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
                writer = csv.DictWriter(csvFile, fieldnames=fields)
                writer.writerow(obj)
        except:
            print("error")