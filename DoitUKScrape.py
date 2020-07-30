from selenium import webdriver
import time
import json
from selenium.webdriver.common.action_chains import ActionChains
FILE_NAME = file_path

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)


url = 'https://doit.life/ours/search?ctype=all&categories=117'
pause_time = 3
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get(url)
time.sleep(pause_time)
oppor = []
organisation = []
about = []
lookinfor = []
count = 0
numb = 0
page_count = 0
load_more = '/html/body/app-root/app-site-app-layout/main/app-routing-search-page/app-site-global-search/div/app-site-search-result-list/div[2]/a'
while page_count < 85
    try:
        if page_count > 0:
            for i in range(page_count):
                print("fdgdgg")
                load_more_button = driver.find_element_by_xpath(load_more)
                load_more_button.click()
                time.sleep(3)
        numb += 1
        print(numb,page_count)
        li = f'/html/body/app-root/app-site-app-layout/main/app-routing-search-page/app-site-global-search/div/app-site-search-result-list/div[1]/app-milestone-def-tile[{count + 1}]/app-milestone-def-tile-cell/article/section/div[1]/div[1]/div[1]/h3'
        ele = driver.find_element_by_xpath(li)
        driver.implicitly_wait(3)
        ActionChains(driver).move_to_element(ele).click(ele).perform()
        count += 1
        print(count)
        time.sleep(pause_time)
        try:
            op = driver.find_element_by_xpath(
                '/html/body/app-root/app-site-app-layout/main/app-site-experience-view-page/div/div/app-modules-milestonedef-view-v1-short-info/article/div[2]/div[1]/div[1]/h1')
            print(op.text)
            oppor.append(op.text)
        except Exception as e:
            oppor.append("Not Found")
        try:
            org = driver.find_element_by_xpath('/html/body/app-root/app-site-app-layout/main/app-site-experience-view-page/div/div/app-modules-milestonedef-view-v1-short-info/article/div[2]/div[1]/div[1]/div/app-common-display-creator-creator/div/span')
            print(org.text)
            organisation.append(org.text)
        except Exception as e:
            organisation.append("Not Found")
        try:
            ab = driver.find_element_by_xpath(
                '/html/body/app-root/app-site-app-layout/main/app-site-experience-view-page/div/app-modules-milestonedef-view-v1-description/section/div/div[2]/div')
            print(ab.text)
            about.append(ab.text)
        except Exception as e:
            about.append("Not Found")
        try:
            lo = driver.find_element_by_xpath(
                '/html/body/app-root/app-site-app-layout/main/app-site-experience-view-page/div/app-modules-milestonedef-view-v1-summary/section/div/div[2]/div')
            print(lo.text)
            lookinfor.append(lo.text)
        except Exception as e:
            lookinfor.append("Not Found")
        but = '/html/body/app-root/app-site-app-layout/main/app-site-experience-view-page/div/div/app-modules-milestonedef-view-v1-short-info/article/div[1]/app-shared-back-btn/button'
        button = driver.find_element_by_xpath(but)
        button.click()
        time.sleep(pause_time)
        if numb > 9:
            page_count += 1
            numb = 0
    except Exception as e:
        break
length = len(oppor)
final_li = []
for i in range(length):
    val = {}
    val['opportunity'] = oppor[i]
    val['organisation'] = organisation[i]
    val['about'] = about[i]
    val['lookinFor'] = lookinfor[i]
    final_li.append(val)
save(final_li)

