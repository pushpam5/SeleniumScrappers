from selenium import webdriver
import time
import json


FILE_NAME = FILE_PATH

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'
url = ["https://monkeypen.com/pages/free-bed-time-stories","https://monkeypen.com/pages/free-stories-for-kids","https://monkeypen.com/pages/free-childrens-picture-books"
       ,"https://monkeypen.com/pages/free-illustrated-childrens-book","https://monkeypen.com/pages/free-bed-time-stories"]
name = []
links = []
val = True
for k in url:
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    driver.get(k)
    #1
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[4]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[4]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #2
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[5]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[5]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #3
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[6]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[6]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #4
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[7]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[7]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #5
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[8]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[8]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #6
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[9]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[9]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #7
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[10]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[10]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #8
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[11]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[11]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #9
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[12]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[12]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    #10
    try :
            v = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[13]/div/h4[2]/strong')
            print(v.text)
            name.append(v.text)
    except:
            name.append("Not Found")
            print("Not Found")
    try:
            but = driver.find_element_by_xpath('/html/body/div[4]/section/div/div[2]/div[13]/div/div[2]/span/a')
            v = but.get_attribute('href')
            print(v)
            links.append(v)
    except:
            links.append("Not Found")
            print("Not Found")
    driver.quit()
print(links)
print(name)
length = len(name)
final_list = []
for i in range(length):
    dict = {}
    dict['bookName'] = name[i]
    dict['DownloadLink'] = links[i]
    final_list.append(dict)
save(final_list)
