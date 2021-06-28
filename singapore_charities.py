from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = 'file_path'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
driver.get('https://www.charities.gov.sg/_layouts/MCYSCPSearch/MCYSCPSearchCriteriaPage.aspx#')
time.sleep(pause_time)

p = driver.find_element_by_id('ctl00_PlaceHolderMain_btnSearch')
p.click()
val = 2
links = []
while val < 468:
    try:
        div = driver.find_elements_by_id('divViewDetail')
        for i in div:
            p = i.find_elements_by_tag_name('input')
            for j in p:
                if j.get_attribute('type') == 'hidden':
                    print(j.get_attribute('value'))
                    links.append(j.get_attribute('value'))
        s = 'a' + str(val)
        k = driver.find_element_by_id(s)
        k.click()
        time.sleep(pause_time - 2)
        print(val)
        val += 1
    except :
        break
for i in links:
    key = {}
    try :
        driver.get(i)
        time.sleep(2)
        na = driver.find_element_by_id('ctl00_PlaceHolderMain_LabelOrgName')
        print(na.text)
        key['organisation'] = na.text
        try:
            web = driver.find_element_by_id('ctl00_PlaceHolderMain_hlWebsite')
            key['website'] = web.get_attribute('href')
            print(key['website'])
        except:
            key['website'] = '-'
        try:
            add = driver.find_element_by_id('ctl00_PlaceHolderMain_lblAddress')
            key['address'] = add.text
            print(add.text)
        except:
            key['address'] = '-'
        try:
            em = driver.find_element_by_id('ctl00_PlaceHolderMain_hlEmailAddress')
            key['Email'] = em.text
            print(em.text)
        except:
            key['Email'] = '-'
        try:
            tele = driver.find_element_by_id('ctl00_PlaceHolderMain_lblTelephoneNo')
            key['tele'] = tele.text
            print(tele.text)
        except:
            key['tele'] = '-'
        try:
            act = driver.find_element_by_id('ctl00_PlaceHolderMain_lblProgramsActivities')
            key['Activities'] = act.text
            print(act.text)
        except:
            key['Activities'] = '-'
        try:
             obj = driver.find_element_by_id('ctl00_PlaceHolderMain_lblObjective')
             key['Objective'] = obj.text
             print(obj.text)
        except:
            key['Objective'] = '-'
        with open(FILE_NAME) as file:
            data = json.load(file)
            data.append(key)
            save(data)
        print(key)
    except Exception as e:
        print(e)