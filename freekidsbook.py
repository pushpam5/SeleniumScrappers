from selenium import webdriver
import time
import json
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

FILE_NAME = f'file_path'
DRIVER_PATH = 'driver_path'

count = 1

pause_time = 2
name = []
links = []
while count < 41:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    if count == 1:
        main_url = 'https://freekidsbooks.org/'
        driver.get(main_url)
    else:
        url = f'https://freekidsbooks.org/page/{count}/'
        driver.get(url)
    li = driver.find_elements_by_class_name('book_header')
    for i in li:
        try:
            k = i.find_element_by_tag_name('a').text
            print(k)
            name.append(k)
        except:
            print("Not Found")
            name.append("Not Found")
    link = driver.find_elements_by_class_name('download-book')
    v = []
    for i in link:
        print(i.get_attribute('id'))
        if i.get_attribute('id')!= "":
            v.append(i)
    print(len(v))
    for i in v:
        try:
            print(i.get_attribute('href'))
            links.append(i.get_attribute('href'))
        except:
            print("Not Found")
            links.append("Not Found")
    time.sleep(pause_time)
    count += 1
    print(len(name),len(links))
    driver.quit()
print(name)
print(links)
length = len(name)
final_list = []
for i in range(length):
    dict = {}
    dict['bookName'] = name[i]
    dict['DownloadLink'] = links[i]
    final_list.append(dict)
save(final_list)
print(2**32)