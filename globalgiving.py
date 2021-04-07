from selenium import webdriver
import time
import json

FILE_NAME = filename
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
links = []
pause_time = 3
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
url = 'https://www.globalgiving.org/search/?size=25&nextPage=1&sortField=sortorder&selectedCountries=00austri&selectedCountries=00belgiu&selectedCountries=00brazil&selectedCountries=00hongko&selectedCountries=00italy&selectedCountries=00mexico&selectedCountries=00russia&selectedCountries=00soukor&selectedCountries=00switze&selectedCountries=00thaila&loadAllResults=true'
driver.get(url)
time.sleep(5)
# button = driver.find_element_by_xpath('/html/body/div[2]/section/div/div/div[2]/div[51]/a')
while True:
    try:
        button = driver.find_element_by_class_name('box_verticalMargin4')
        button.click()
        time.sleep(4)
    except:
        break
ele = driver.find_elements_by_class_name('grid-lg-8')
oppor = []
links = []
for i in ele:
    try:
        head = i.find_element_by_tag_name('h4')
        oppor.append(head.text)
        print(head.text)
        lin = head.find_element_by_tag_name('a')
        print(lin.get_attribute('href'))
        links.append(lin.get_attribute('href'))
    except:
        print("error")
print(len(links),len(oppor))
for i in range(len(links)):
    obj = {}
    try:
        obj['oppor'] = oppor[i]
        obj['link'] = links[i]
        driver.get(links[i])
        org_name = driver.find_element_by_tag_name('h3')
        print(org_name.text)
        obj['org_name'] = org_name.text
        org_link = org_name.find_element_by_tag_name('a')
        print(org_link.get_attribute('href'))
        obj['org_link'] = org_link.get_attribute('href')
        # details = driver.find_element_by_class_name('text_fontSizeSmall')
        det = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[5]/div/div[1]/div')
        print(det.text)
        obj['details'] = str(det.text).split('\n')
    except:
        print("error")
    print(obj)
    with open(FILE_NAME) as file:
        data = json.load(file)
        data.append(obj)
        save(data)