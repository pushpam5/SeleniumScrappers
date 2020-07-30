from selenium import webdriver
import time
import json


FILE_NAME = file_path
FILE_NAME1 = file_path
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

def savelink(x):
    with open(FILE_NAME1,'w') as f:
        json.dump(x,f)

pause_time = 3
DRIVER_PATH = 'chromedriver.exe'
links = []
final_orglinks = []
org_link = []
emails = []
contactNo = []
opportunities = []
organisations = []
expirydate = []
emails = []
contactNo = []
listedBy = []
val = 0
while val < 41:

    try:
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get('https://www.i-vol.ie/organisation-search/?pageNumber=' + str(val))
        time.sleep(pause_time)
        print(val)
        h = driver.find_elements_by_tag_name('a')
        for j in h:
            if j.get_attribute('class') == "" and j.text == "View Organisation >>":
                    links.append(j.get_attribute('href'))
        print(links)
        driver.quit()
        for j in links:
            driver = webdriver.Chrome(executable_path=DRIVER_PATH)
            driver.get(j)
            h1 = driver.find_elements_by_tag_name('a')
            for j in h1:
                if j.get_attribute('class') == "" and j.text == "View":
                    org_link.append(j.get_attribute('href'))
            driver.quit()
        for j in org_link:
            driver = webdriver.Chrome(executable_path=DRIVER_PATH)
            driver.get(j)
            time.sleep(pause_time)
            try:
                oppor = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/h1')
                opportunity = oppor.text
            except Exception as e:
                opportunity = "Not Found"
            try:
                org = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/h2')
                organisation = org.text
                print(organisation)
            except Exception as e:
                organisation = "Not Found"
            try:
                em = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/ul/li[2]/a')
                email = em.text
                print(email)

            except Exception as e:
                email = "Not Found"
            try:
                con = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/ul/li[3]/a')
                contact = con.text
                print(contact)

            except Exception as e:
                contact = "Not Found"
            try:
                exp = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div[1]/h3[2]')
                expiry = exp.text
                print(expiry)

            except Exception as e:
                expiry = "Not Found"
            try:
                list = driver.find_element_by_xpath('/html/body/div[1]/div[2]/main/div/section/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[2]/div/ul/li[1]/strong')
                listed = list.text
                print(listed)

            except Exception as e :
                listed = "Not Found"
            emails.append(email)
            organisations.append(organisation)
            opportunities.append(opportunity)
            contactNo.append(contact)
            listedBy.append(listed)
            expirydate.append(expiry)
            driver.quit()
        val += 1
        links = []
        final_orglinks.extend(org_link)
        org_link = []
    except Exception as e:
        print(e)
        break
final_list = []
length = len(emails)
for i in range(length):
    dict = {}
    dict['opportunity'] = opportunities[i]
    dict['organisation'] = organisations[i]
    dict['expiry_date'] = expirydate[i]
    dict['email'] = emails[i]
    dict['contactNo.'] = contactNo[i]
    dict['ListedBy'] = listedBy[i]
    final_list.append(dict)
save(final_list)
savelink(org_link)

