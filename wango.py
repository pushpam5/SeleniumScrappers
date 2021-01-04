from selenium import webdriver
import time
import json
import re
from selenium.webdriver.support.ui import Select

FILE_NAME = FILE_PATH
phone = []
fax = []
email = []
address = []
city = []
zip = []
country = []
activity = []
membership = []
type = []
website = []
name = []
org_level = []
typeco = []
member = []
wango = []

with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
pause_time = 3
val = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.wango.org/members.aspx')
username = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')
button = driver.find_element_by_name('login')
username.send_keys(username)
password.send_keys(password)
button.click()
driver.get('https://www.wango.org/members.aspx?section=ngodir')
p = driver.find_element_by_class_name("postActive")
p.click()

sel = Select(driver.find_element_by_name("search_regionID"))
sel.select_by_value('15')

sel = Select(driver.find_element_by_name("search_country"))
sel.select_by_value('Morocco')
but = driver.find_element_by_name('submitbutton')
but.click()
links = []
ids = []
k = 1
leng = NUMBER_OF_PAGES
while k <= leng:
    links = []
    ids = []
    if k != 1:
        j = driver.find_elements_by_tag_name('a')
        for i in j:
            s = f"javascript:goPage('{k}',  '', 'zz');void(0);"
            print(i.get_attribute('href'),f"javascript:goPage('{k}',  '', 'zz');void(0);")
            if str(i.get_attribute('href')) == str(f"javascript:goPage('{k}',  '', 'zz');void(0);"):
                i.click()
                break
    p = driver.find_elements_by_tag_name('a')
    name = []
    for i in p:
        if 'javascript:loadOrg' in i.get_attribute('href'):
            name.append(i.text)
            links.append(i)
    print(name)
    time.sleep(1)
    for i in links:
        ids.append(''.join(re.findall(r'\d+',str(i.get_attribute('href')))))
    print(ids)
    count = 0
    tot = 0
    for i in links:
        i.click()
        print(f'd{ids[tot]}')
        p = driver.find_element_by_id(f'd{ids[tot]}')
        q = p.find_elements_by_class_name('tdbgray')
        length = len(q)
        l = []
        s = "name : "
        s += name[tot]
        l.append(s)
        for i in range(length):
            if i & 1 == 0:
                s = q[i].text
                print(s)
            else:
                s += f' : {q[i].text} '
                print(s)
                l.append(s)
        with open(FILE_NAME) as file:
            data = json.load(file)
            data.append(l)
            save(data)
        tot += 1
    k += 1
