from selenium import webdriver
import time
import json
import re

FILE_NAME = filename
organisation = []
org_link = []
email = []
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
url = 'http://www.ivolunteer.org.il/Eng/Index.asp?CategoryID=128'
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

driver.get(url)
time.sleep(3)
p = driver.find_element_by_id('ctlContent')
ele = p.find_elements_by_tag_name('td')
for i in ele:
    try:
        al = i.find_element_by_tag_name('a')
        if al.text != '':
            if al.text not in organisation and al.text != 'international':
                organisation.append(al.text)
                org_link.append(al.get_attribute('href'))
    except:
        print("error")
print(org_link)
print(organisation)
print(len(organisation))
driver.quit()
count = 0
for i in org_link:
    print(count + 1)
    try:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(i)
        l = {}
        p = driver.find_element_by_id('ctlContent')
        try:
            v = p.find_element_by_tag_name('tbody')
            e = re.findall('\S+@\S+', v.text)
            print(e)
            k = []
            if len(e) == 0:
                k = 'Not Found'
            else:
                k = e
            s = v.text
            print(k)
            l['name'] = organisation[count]
            l['email'] = k
            l['org_link'] = i
            l['details'] = s
            with open(FILE_NAME) as file:
                data = json.load(file)
                data.append(l)
                save(data)
        except:
            l['name'] = organisation[count]
            l['org_link'] = i
            l['details'] = "Not Found"
            l['email'] = "Not Found"
            with open(FILE_NAME) as file:
                data = json.load(file)
                data.append(l)
                save(data)
            print("error")
    except:
        print("e")
        l['name'] = organisation[count]
        l['org_link'] = i
        l['details'] = "Not Found"
        l['email'] = "Not Found"
        with open(FILE_NAME) as file:
            data = json.load(file)
            data.append(l)
            save(data)
        print("error")
    count += 1
    driver.quit()
    time.sleep(2)