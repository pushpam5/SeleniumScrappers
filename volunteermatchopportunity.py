from selenium import webdriver
import time
import json

FILE_NAME = FILE_PATH

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 3
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://www.volunteermatch.org/search/?l=Oman'
driver.get(url)
time.sleep(3)
v = driver.find_elements_by_tag_name('a')
li = []
for i in v:
    if i.get_attribute('class') == 'link-body-text pub-srp-opps__title ga-track-to-opp-details':
        li.append(i)
opportunities_link = []
for i in li:
    opportunities_link.append(i.get_attribute('href'))
driver.quit()
oppor = []
org = []
org_link = []
interest = []
skills = []
good_for = []
description = []
mission = []
summary  = []
location = []
requirements = []
for j in opportunities_link:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(j)
    time.sleep(3)
    try:
        opp = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[2]/section[1]/h2')
        print(opp.text)
        oppor.append(opp.text)
    except Exception as e:
        print(e)
        oppor.append("Not Found")
    try:
        orgname = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[2]/section[1]/p/a')
        print(orgname.text)
        print(orgname.get_attribute('href'))
        org.append(orgname.text)
        org_link.append(orgname.get_attribute('href'))
    except Exception as e:
        print(e)
        org.append("Nor Found")
        org_link.append("Nor Found")
    try:
        intre = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[2]/section[1]/ul/li[6]/div')
        print(intre.text)
        interest.append(intre.text)
    except Exception as e:
        print(e)
        interest.append("Not Found")
    try:
        sk = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[3]/div/div[2]/section[1]/ul')
        print(sk.text)
        val = str(sk.text)
        skills.append(val.split('\n'))
    except Exception as e:
        print(e)
        skills.append("Not Found")
    try:
        go = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[3]/div/div[2]/section[2]/ul')
        print(go.text)
        good_for.append(str(go.text).split('\n'))
    except Exception as e:
        print(e)
        good_for.append("Not Found")
    try:
        req = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[3]/div/section[4]/ul')
        print(req.text)
        val = list(str(req.text).split('\n'))
        requirements.append(val)
    except Exception as e:
        print(e)
        requirements.append("Not Found")
    try:
        add = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[3]/div/section[2]/div[1]')
        print(add.text)
        location.append(add.text)
    except Exception as e:
        print(e)
        location.append("Not Found")
    try:
        mis = driver.find_element_by_xpath('/html/body/div[5]/div[2]/main/div/div[2]/section[3]/p[2]')
        print(mis.text)
        mission.append(mis.text)
    except Exception as e:
        print(e)
        mission.append("Not Found")
    try:
        el = driver.find_element_by_id('short_desc')
        print(el.text)
        summary.append(str(el.text))
    except Exception as e:
        print("Summary not found")
        try:
            ele = driver.find_element_by_id('condensed_short_desc')
            print(ele.text)
            summary.append(str(ele.text))
        except Exception as e:
            print(e)
            summary.append("Not Found")
    try:
        el = driver.find_element_by_id('tertiary-content')
        val = str(el.text)
        print(el.text)
        description.append(val)
    except Exception as e:
        print(e)
        description.append("Not Found")
    driver.quit()
final_list = []
length = len(opportunities_link)
for i in range(length):
    dict = {}
    dict['opportunity'] = oppor[i]
    dict['opportunity_link'] = opportunities_link[i]
    dict['organisation'] = org[i]
    dict['org_link'] = org_link[i]
    dict['skills_Required'] = skills[i]
    dict['interested'] = interest[i]
    dict['good_for'] = good_for[i]
    dict['requirements'] = requirements[i]
    dict['mission_Statement'] = mission[i]
    dict['Description'] = description[i]
    dict['summary'] = summary[i]
    dict['address'] = location[i]
    final_list.append(dict)
save(final_list)
