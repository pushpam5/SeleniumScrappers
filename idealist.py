from selenium import webdriver
import time
import csv
import json
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import Select

DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
cntry = ["Mexico"]
try:
    for cou in cntry:
        FILE_NAME = f'file_path'
        pause_time = 2

        driver.get('https://www.idealist.org/en/organizations?orgType=NONPROFIT&orgType=SOCIAL_ENTERPRISE&q=&searchMode=true')
        time.sleep(5)

        button = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[4]/div/div/button')
        button.click()
        country = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div/div/div/div[1]/div[2]/div/div/div/div/div[4]/div/div/div/div/div/div[1]/div/input')
        country.clear()
        country.send_keys(cou)
        time.sleep(3)
        country.send_keys(Keys.ENTER)
        time.sleep(3)
        links = []
        a = driver.find_element_by_class_name('eiRYej')
        a.click()
        count = 0
        time.sleep(4)
        li = []
        with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
            fields = ['name', 'link', 'areas', 'details']
            writer = csv.DictWriter(csvFile, fieldnames=fields)
            writer.writeheader()
            csvFile.close()
        while True:
            try:
                obj = {}
                try:
                    head = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[1]/div/div[2]/h1')
                    print(head.text)
                    obj['name'] = head.text
                except:
                    obj['name'] = '-'
                try:
                    lin = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[1]/div/div[3]/a')
                    print(lin.get_attribute('href'))
                    obj['link'] = lin.get_attribute('href')
                except:
                    obj['link'] = '-'
                try:
                    area = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[3]/div/div[2]')
                    print(area.text)
                    obj['areas'] = str(area.text).split('\n')
                except:
                    obj['areas'] = '-'
                try:
                    det = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[3]/div/div[3]')
                    print(det.text)
                    obj['details'] = str(det.text).split('\n')
                    print(obj['details'])
                except:
                    obj['details'] = '-'
                print(obj)
                li.append(obj)
                with open(FILE_NAME, 'a', encoding="utf-8") as csvFile:
                    writer = csv.DictWriter(csvFile, fieldnames=fields)
                    writer.writerow(obj)
                if count == 0:
                    but = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[3]/span/div/div/div/div/a/div')
                else:
                    but = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[6]/div/div/div[3]/span/div/div/div/div/a[2]/div')
                but.click()
                time.sleep(3)
                count += 1
            except :
                break
except Exception as e:
    print(e)
    print(cou)