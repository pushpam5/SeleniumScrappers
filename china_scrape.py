from selenium import webdriver
import time
import json

FILE_NAME = f'file_path'

with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
links = []
pause_time = 3
DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
links = []
names = []
page = 1
while page < 29:
    driver.get(f'https://chinadevelopmentbrief.cn/ngo-directory/?tab=search-form&pg={page}&sort=a-z')
    time.sleep(4)
    elements = driver.find_elements_by_class_name('grid-item')
    for i in elements:
        head = i.find_element_by_class_name('lf-item')
        link = head.find_element_by_tag_name('a')
        links.append(link.get_attribute('href'))
        n = link.find_element_by_tag_name('h4')
        names.append(n.text)
    page += 1
print(links)
print(len(links),len(names))
count = 0
for i in links:
    obj = {}
    obj['name'] = names[count]
    obj['links'] = links[count]
    driver.get(i)
    time.sleep(3)
    try:
        ele = driver.find_element_by_class_name('block-field-ngo-contact-information')
        det = ele.find_element_by_class_name('pf-body')
        print(det.text)
        obj['details'] = str(det.text).split('\n')
        print(obj)
    except:
        obj['details'] = '-'
        print("error")
    with open(FILE_NAME) as file:
        data = json.load(file)
        data.append(obj)
        save(data)
    count += 1