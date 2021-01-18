from selenium import webdriver
import time
import json
import re

FILE_NAME = 'FILE_PATH'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
url = "https://www.allforgood.org/search?expandFavorites=false&getRemote=true&radiusDropdown=within%2050%20miles"
links = []
names = []
details = []
address = []
driver.get(url)
time.sleep(pause_time + 5)
c = 1
while c <= 670:
    try:
        c += 1
        p = driver.find_element_by_class_name('search-footer')
        load_more = p.find_element_by_tag_name('a')
        # for i in p:
        #     if i.get_attribute('data-ember-action-467') == "467":
        #         load_more = i
        #         break
        load_more.click()
        time.sleep(pause_time + 3)
        print(c)
    except:
        break
a = driver.find_elements_by_class_name('search-card')
for i in a:
    li = i.find_elements_by_tag_name('a')
    for j in li:
        if j.get_attribute('class') == 'pb-link-sm ember-view':
            # print(j.get_attribute('href'))
            links.append(j.get_attribute('href'))
            # print(j.text)
            names.append(j.text)
    try:
        k = i.find_element_by_class_name('description')
        # print(k.text)
        details.append(k.text)
    except:
        details.append("-")
    try:
        f = i.find_elements_by_tag_name('p')
        for j in f:
            if j.get_attribute('class') == 'pb-copy-sm':
                print(j.text)
                address.append(j.text)
    except:
        address.append("-")
organisation = []
org_link = []
email = []
impact_area = []
mobile = []
count = 0
for i in links:
    print(count + 1)
    print(i)
    driver.get(i)
    time.sleep(3)
    flg = False
    try:
        a = driver.find_element_by_class_name("pb-link")
        print(a.text)
        organisation.append(a.text)
        org_link.append(a.get_attribute('href'))
    except:
        org_link.append("-")
        organisation.append("-")
    try:
        flg = True
        a = driver.find_elements_by_tag_name('article')
        for j in a:
            if j.get_attribute('class') == "show-contact-info":
                k = str(j.text).split("\n")
                l = re.findall('\S+@\S+', j.text)
                print(l)
                if len(l) == 0:
                    email.append("-")
                else:
                    email.append(l)
                mflag = False
                for i in k:
                    if i.isnumeric():
                        print(i)
                        mobile.append(i)
                        mflag = True
                        break
                if not mflag:
                    mobile.append("-")
    except:
        print("Null")
        email.append("-")
        mobile.append("-")
    try:
        a = driver.find_elements_by_tag_name('section')
        for j in a:
            if j.get_attribute('class') == "service-box":
                l = str(j.text).split("\n")
                l = l[1:]
                print(l)
                if len(l) == 0:
                    impact_area.append("-")
                else:
                    impact_area.append(l)
    except:
        print("NULL")
        impact_area.append("-")
    if len(email) - 1 < count:
        email.append("-")
    if len(mobile) - 1 < count:
        mobile.append("-")
    if len(org_link) - 1 < count:
        org_link.append("-")
    if len(organisation) - 1< count:
        organisation.append("-")
    if len(impact_area) - 1< count:
        impact_area.append("-")
    with open(FILE_NAME) as file:
        data = json.load(file)
    va = {}
    try:
        va['name'] = names[count]
        va['link'] = links[count]
        va['organisation'] = organisation[count]
        va['org_link'] = org_link[count]
        va['email'] = email[count]
        va['impact_areas'] = impact_area[count]
        va['phone'] = mobile[count]
        va['details'] = details[count]
        va['address'] = address[count]
        data.append(va)
        save(data)
        count += 1
    except:
        print(count)
