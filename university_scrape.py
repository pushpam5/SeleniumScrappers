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
DRIVER_PATH = 'driver_path'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.university-directory.eu/js/north_american-universities.html')
elements = driver.find_elements_by_class_name('university-directory')
links = []
for i in elements:
    a = i.get_attribute('href')
    links.append(a)
l = links[0]
for j in links:
    driver.get(j)
    try:
        partner = driver.find_elements_by_class_name('partnerlist')
        a = partner[1]
        title = []
        link = []
        elel = a.find_elements_by_class_name('row')
        for k in elel:
            try:
                li = k.find_element_by_class_name('partnermiddle')
                p = li.find_element_by_tag_name('a')
                title.append(p.get_attribute('title'))
                link.append(p.get_attribute('href'))
            except:
                print("error")
        for i in link:
          obj = {}
          driver.get(i)
          try:
              rows = driver.find_elements_by_class_name('univer_cont_detail')
              for j in rows:
                  try:
                      key = j.find_element_by_class_name('cont_title').text
                      value = j.find_element_by_class_name('cont_info').text
                      obj[key] = value
                  except:
                      print("error")
          except:
              print("error")
          # print(obj)
          with open(FILE_NAME) as file:
              data = json.load(file)
              data.append(obj)
              save(data)
          print(obj)
    except:
        print("error")