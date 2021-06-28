from selenium import webdriver
import time
import csv
import re

FILE_NAME = f'file_path'

with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
    fields = ['NGO','NGO_Link','address','website','email','Contact_Person']
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    csvFile.close()


DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

url = 'https://ngobridges.com/ngo?countries%5B%5D=4'
driver.get(url)
time.sleep(3)
ngo = []
ngo_link = []
val = 1
while val < 9:
    if val != 1:
        driver.get(f'https://ngobridges.com/ngo?countries%5B0%5D=4&page={val}')
        time.sleep(3)
    divisions = driver.find_elements_by_class_name('company')
    for i in divisions:
        head = i.find_element_by_tag_name('h4')
        a = head.find_element_by_tag_name('a')
        print(a.text)
        print(a.get_attribute('href'))
        ngo.append(a.text)
        ngo_link.append(a.get_attribute('href'))
    val += 1
length = len(ngo)
for i in range(length):
    obj = {}
    obj['NGO'] = ngo[i]
    obj['NGO_Link'] = ngo_link[i]
    try:
        driver.get(ngo_link[i])
        time.sleep(3)
        pro = driver.find_element_by_class_name('company-profile')
        ele = pro.find_elements_by_class_name('profile-box')
        try:
            print(ele[0].find_element_by_class_name('profile-content').text)
            obj['address'] = ele[0].find_element_by_class_name('profile-content').text

        except:
            obj['address'] = '-'
        try:
            web = ele[1].find_element_by_class_name('profile-content')
            a = web.find_element_by_tag_name('a')
            print(a.get_attribute('href'))
            obj['website'] = a.get_attribute('href')
        except:
            obj['website'] = '-'
        try:
            print(ele[2].find_element_by_class_name('profile-content').text)
            obj['email'] = ele[2].find_element_by_class_name('profile-content').text
        except:
            obj['email'] = ['-']
        try:
            print(ele[3].find_element_by_class_name('profile-content').text)
            obj['Contact_Person'] = ele[3].find_element_by_class_name('profile-content').text
        except:
            obj['Contact_Person'] = '-'
        print(obj)
        with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writerow(obj)
    except:
        continue