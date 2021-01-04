from selenium import webdriver
import time
import json


FILE_NAME = 'C:\\Users\\RealMe\\PycharmProjects\\codes\\storyweaverstoriesmarathi.json'

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'

links = []
names = []
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
url = 'https://storyweaver.org.in/stories?language=Marathi&query=&sort=Ratings'
driver.get(url)
time.sleep(pause_time + 7)
count = 1
while True:
    try:
        p = driver.find_element_by_class_name('pb-button--size-m')
        time.sleep(5)
        print(count)
        p.click()
    except Exception as e:
        print(e)
        print("End")
        break
    count += 1
k = driver.find_elements_by_tag_name('a')
for i in k:
    try:
        if i.get_attribute('class') == 'pb-link pb-link--default pb-book-card__link':
            val = i.get_attribute('href')
            print(val)
            links.append(val)
    except:
        links.append("Not Found")
h = driver.find_elements_by_tag_name('h3')
for i in h:
    try:
        if i.get_attribute('class') == 'pb-book-card__title':
            te = i.text
            print(te)
            names.append(te)
    except:
        names.append("Not Found")
driver.quit()
print(names)
print(links)
print(len(names),len(links))
publisher = []
language = []
categories = []
type = []
level = []
count = 0
for i in links:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.set_window_position(0, 0)
    driver.set_window_size(1920, 1080)
    driver.get(i)
    time.sleep(10)
    print(count + 1)
    try:
        spans = driver.find_elements_by_tag_name('span')
        flag1,flag2 = False,False
        for i in spans:
            if not flag1:
                if i.get_attribute('class') == 'pb-book-card__language':
                    language.append(i.text)
                    flag1 = True
                    print(i.text)
            if not flag2:
                if i.get_attribute('class') == 'pb-book-card__level':
                    print(i.text)
                    flag2 = True
                    level.append(i.text)
        if not flag1:
            language.append("Not Found")
        if not flag2:
            level.append("Not Found")
    except Exception as e:
        print(e)
        if not flag1:
            language.append("Not Found")
        if not flag2:
            level.append("Not Found")
    try:
        para = driver.find_element_by_class_name('pb-publisher')
        paraf = para.find_element_by_tag_name('p')
        print(paraf.text)
        publisher.append(paraf.text)
    except Exception as e:
        print(e)
        publisher.append("Not Found")
    try:
        k = driver.find_element_by_class_name('pb-book__tags-wrapper')
        uli = k.find_elements_by_tag_name('ul')
        f1,f2 = False,False
        for i in uli:
            if not f1 or not f2:
                if i.get_attribute('class') == 'pb-list pb-list--inline':
                    p = []
                    vli = i.find_elements_by_tag_name('li')
                    for j in  vli:
                        print(j.text)
                        p.append(j.text)
                    if f1 and not f2:
                        categories.append(p)
                        f2 = True
                    if not f1:
                        type.append(p)
                        f1 = True
            else:
                break
        if not f1:
            type.append("Not Found")
        if not f2:
            categories.append("Not Found")
    except Exception as e:
        print(e)
        type.append("Not Found")
        categories.append("Not Found")
    driver.quit()
    with open(FILE_NAME) as file:
        data = json.load(file)
    va = {}
    va['name'] = names[count]
    va['link'] = links[count]
    va['publisher'] = publisher[count]
    va['language'] = language[count]
    va['level'] = level[count]
    va['categories'] = categories[count]
    va['type'] = type[count]
    data.append(va)
    save(data)
    count += 1
# final_list = []
# for i in range(count):
#     va = {}
#     va['name'] = names[i]
#     va['link'] = links[i]
#     va['publisher'] = publisher[i]
#     va['language'] = language[i]
#     va['level'] = level[i]
#     va['categories'] = categories[i]
#     va['type'] = type[i]
#     final_list.append(va)
# save(final_list)