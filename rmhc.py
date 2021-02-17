from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import pycountry

FILE_NAME = 'C:\\Users\\RealMe\\PycharmProjects\\codes\\rmhc1.json'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
pause_time = 3
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
driver.get('https://www.rmhc.org/find-a-chapter')
sel = Select(driver.find_element_by_id('radiusDropdown'))
sel.select_by_value('300')
a = (list(pycountry.countries))
button = driver.find_element_by_id('findAChapterListSearch')
ind = 0
for i in range(len(a)) :
    if a[i].name == "Saint Martin (French part)":
       ind = i
       break
print(len(a))
for i in a[ind + 1:]:
    country = driver.find_element_by_class_name('tt-input')
    country.send_keys(Keys.CONTROL + "a");
    country.send_keys(Keys.DELETE);
    country.send_keys(i.name)
    button.click()
    time.sleep(pause_time + 5)
    try:
        val = driver.find_element_by_id('resultCount')
        if val.text != '0':
            print("fgggfgfg")
            v = driver.find_elements_by_class_name('find-a-chapter-results-card')
            print(len(v))
            for j in v:
                inner = j.find_element_by_class_name('inner-container')
                print(i.name)
                head = inner.find_element_by_class_name("right-col")
                p = {}
                p['country'] = i.name
                try:
                    print("fhghfhf")
                    org_name = head.find_element_by_tag_name('h5').text
                    print(org_name)
                    p['org_name'] = org_name
                except:
                    p['org_name'] = "Not Found"
                try:
                    add = head.find_element_by_tag_name('p')
                    print(add.text)
                    address = add.text
                    p['address'] = str(address).rstrip('\n')
                    try:
                        phone = add.find_element_by_tag_name('b')
                        print(phone.text)
                        p['phone'] = phone.text
                    except:
                        p['phone'] = "Not Found"
                except:
                    p['address'] = "Not Found"
                try:
                    health = head.find_element_by_tag_name('span')
                    print(health.text)
                    p['health_care'] = health.text
                except:
                    p['health_care'] = 'Not Found'
                try:
                    web = head.find_element_by_class_name("address-url")
                    li = web.find_element_by_tag_name('a')
                    print(li.get_attribute('href'))
                    p['website'] = li.get_attribute('href')
                except:
                    p['website'] = "Not Found"
                    print("Not Found")
                print(p)
                with open(FILE_NAME) as file:
                    data = json.load(file)
                    data.append(p)
                    save(data)
    except Exception as e:
        print(e)
        print("Error Occured")