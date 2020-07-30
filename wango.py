from selenium import webdriver
import time
import json
FILE_NAME = file_path


def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
organisation = []
address = []
details = []
pause_time = 3
val = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://www.wango.org/resources.aspx?section=ngodir&sub=list&regionID=0&col=')
loaddata = '/html/body/div[1]/div/div[2]/div[2]/table/tbody/tr/td[1]/a[1]'
while True and val < 200:

    time.sleep(pause_time)
    try:
        add = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/table/tbody/tr/td[1]/div[3]/div[1]')
        print(add.text)
        address.append(add.text)
    except Exception as e:
        address.append("Not Found")
    try:
        h = driver.find_element_by_xpath(loaddata)
        h.click()
    except:
        break
    try:
        org = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/table/tbody/tr/td[1]/a[1]/b')
        print(org.text)
        organisation.append(org.text)
    except Exception as e:
        organisation.append("Not Found")
    try:
        det = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/table/tbody/tr/td[1]/div[4]/div/table/tbody/tr[1]/td/div')
        print(det.text)
        details.append(det.text)
    except Exception as e:
        details.append("Not Found")
    try:
        print(f"javascript:goPage('{val}',  '', 'zz');void(0);")
        link = driver.find_elements_by_tag_name('a')
        for j in  link:
            if j.get_attribute('href') == f"javascript:goPage('{val}',  '', 'zz');void(0);":
                next_button = j
        next_button.click()
        val += 1
    except Exception as e:
        val+= 1
print(address)
print(organisation)

final_list = []
length = len(address)
print(val)
for j in range(length):
    dict = {}
    dict['address'] = address[j]
    dict['organisation'] = organisation[j]
    dict['details'] = details[j]
    final_list.append(dict)
print(final_list)
save(final_list)

