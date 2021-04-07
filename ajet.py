from selenium import webdriver
import time
import json
FILE_NAME = filename


def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)


url = 'https://ajet.net/jet-community/volunteering-charity/volunteer-in-japan/'
pause_time = 4
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(pause_time)

organisation = []
descrip = []
contactinfo = []
cl_links = []
text = []

val = driver.find_elements_by_tag_name('td')
for i in val:
    if i.get_attribute('class') == 'column-1':
        print(i.text)
        organisation.append(i.text)
    elif i.get_attribute('class') == 'column-2':
        print(i.text)
        descrip.append(i.text)
    elif i.get_attribute('class') == 'column-3':
        links = i.find_elements_by_tag_name('a')
        text.append(i.text)
        link = []
        for j in links:
            if j.get_attribute('class') == 'mailto-link':
                print(j.get_attribute('data-enc-email'))
                link.append(j.get_attribute('data-enc-email'))
            else:
                print(j.get_attribute('href'))
                link.append(j.get_attribute('href'))
        cl_links.append(link)
length = len(organisation)
final_li = []
for i in range(length):
    val = {}
    val['organisation'] = organisation[i]
    val['description'] = descrip[i]
    val['clicklinks'] = cl_links[i]
    val['details'] = text[i]
    final_li.append(val)
save(final_li)
print(final_li)