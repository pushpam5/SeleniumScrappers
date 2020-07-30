from selenium import webdriver
import time
import json
FILE_NAME = file_path
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

city = ['Antrim', 'Armagh', 'Carlow', 'Cavan', 'Clare', 'Cork', 'Derry', ' Donegal', 'Down', 'Dublin', 'Fermanagh', 'Galway', 'Kerry', ' Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath', 'Monaghan', 'Offaly', ' Roscommon', 'Sligo', 'Tipperary', ' Tyrone', 'Waterford', 'Westmeath', 'Wexford', ' Wicklow']
pause_time = 1
DRIVER_PATH = 'chromedriver.exe'
i = 1
charities = []
sites = []
emails = []
phone_no = []
addresses = []
for ci in city:
    print(ci)
    url = f'https://rip.ie/services/{ci}/Charities'
    i = 1
    while True:
        try:
            driver = webdriver.Chrome(executable_path=DRIVER_PATH)
            driver.get(url)
            try:
                more_info = driver.find_element_by_xpath(f'/html/body/div[2]/div[3]/div[2]/section[1]/div/div[2]/ul/li[{i}]/div[1]/div[4]/div/form/button')
                more_info.click()
                time.sleep(pause_time)
                try:
                    charity = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section[1]/div/div/h2')
                    charities.append(charity.text)
                except Exception as e:
                    charities.append("Not Found")
                    print(e)

                try:
                    link = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section[2]/div/div[1]/ul[2]/li[1]/a')
                    sites.append(link.text)
                    print(link.text)

                except Exception as e:
                    sites.append("Not Found")
                    print(e)

                try:
                    email = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section[2]/div/div[1]/ul[2]/li[2]/a')
                    emails.append(email.text)
                    print(email.text)

                except Exception as e:
                    emails.append("Not Found")
                    print(e)

                try:
                    phone = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section[2]/div/div[1]/ul[2]/li[3]')
                    phone_no.append(phone.text)
                    print(phone.text)

                except Exception as e:
                    print(e)
                    phone_no.append("Not Found")
                try:
                    add = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/section[2]/div/div[1]/ul[3]/li/p[1]')
                    addresses.append(add.text)
                    print(add.text)

                except Exception as e:
                    print(e)
                    addresses.append("Not Found")

                i += 1
                print(i)
                driver.quit()
            except Exception as e:
                print(e)
                break
        except Exception as e:
            print(e)
            break
final_list = []
print(charities)
print(emails)
print(sites)
print(addresses)
print(phone_no)
length = len(sites)
for i in range(length):
    dict = {}
    dict['charity'] = charities[i]
    dict['email'] = emails[i]
    dict['phone_no'] = phone_no[i]
    dict['link'] = sites[i]
    dict['address'] = addresses[i]
    final_list.append(dict)
print(final_list)
save(final_list)

