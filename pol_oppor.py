from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = filename

with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get('https://engage.pointsoflight.org/search/i/?area=Thailand&aroundRadius=all&aroundLatLng=15.87%252C100.993')
time.sleep(5)
links = []
opportunity = []
count = 0
while count < 100:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(3)
    count += 1
lis = driver.find_elements_by_tag_name('ul')
print(lis)
for i in lis:
    k = i.find_elements_by_tag_name('li')
    for j in k:
        link = j.find_element_by_tag_name('a')
        print(link.get_attribute('href'))
        links.append(link.get_attribute('href'))
        print(str(link.get_attribute('data-ga-label')).split('(')[0])
        opportunity.append(str(link.get_attribute('data-ga-label')).split('(')[0])

length = len(opportunity)
final_list = []
for i in range(length):
    obj = {}
    obj['opportunity'] = opportunity[i]
    obj['link'] = links[i]
    driver.get(links[i])
    try:
        org_name = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/article/header/dl[1]/dd/a').text
        print(org_name)
        obj['org-name'] = org_name
    except:
        obj['org-name'] = '-'
    try:
        org_link = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/article/div/div/div[2]/div[2]/footer/div[1]/div/p/a').get_attribute('href')
        print(org_link)
        obj['org_link'] = org_link
    except:
        obj['org_link'] = '-'
    try:
        details = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/article/div/div/div[2]/div[1]/div').text
        print(details)
        email = re.findall('\S+@\S+', str(details))
        if(len(email) == 0):
            obj["email"] = '-'
        else:
            obj["email"] = email
        phone = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-][2-9][0-9]{2}[-][0-9]{4}\b', str(details))
        if (len(phone) == 0):
            obj["phone"] = '-'
        else:
            obj["phone"] = phone
        obj['details'] = details
    except:
        obj['details'] = '-'
        obj['email'] = '-'
        obj['phone'] = '-'
    print(obj)
    with open(FILE_NAME) as file:
        data = json.load(file)
        data.append(obj)
        save(data)
