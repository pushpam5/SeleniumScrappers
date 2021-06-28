from bs4 import BeautifulSoup
import json
import requests
import argparse
import json



FILE_NAME='file_path'

url = 'https://www.volunteer.com.au/community-services-volunteering?suitablefor=12'

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

try:

    resp=requests.get(url).content
    soup=BeautifulSoup(resp,'html.parser')
    val = soup.find_all('a')
    value = soup.find_all('strong')

    #opportunities
    firm = []
    job = []
    for j in val:
        if j.get('class') != None:
            if j.get('class')[0] == 'search-results__result-body-link':
               job.append(j.contents[0])

    length = len(job)
    for i in range(length):
        job[i] = job[i].lstrip('\r\n').rstrip().lstrip()

    #organisations
    firm_name = []
    for j in value:
        if j.get('class') != None:
            if j.get('class')[0] == 'item-owner':
               firm.append(j.contents[1])
    length = len(firm)
    for j in firm:
        firm_name.append(j.contents[0])
    print(job)
    print(firm_name)

    #links to organisation
    for i in range(length):
        firm[i] = firm[i].get('href')
    links = []
    string = 'https://www.volunteer.com.au/volunteering-organisations'
    for i in range(length):
        link,id = firm[i].split('=')
        stri = string + '/' + id + '/' + firm_name[i]
        links.append(stri)
    print(links)

    #contact Details
    addresses = []
    websites = []
    emails = []

    for url in links:
        URL = url
        resp = requests.get(URL).content
        soup = BeautifulSoup(resp, 'html.parser')
        val = soup.find_all('ul')
        flag = True
        try:
            for v in val:
                flag = True
                if v.get('class')[0] == 'item-info':
                    if v.contents[1].contents[3].contents != None:
                        cont = v.contents[1].contents[3].contents
                        address = ''
                        for add in cont:
                                add = str(add)
                                add = add.lstrip().rstrip()
                                add = add.lstrip('<br/>')
                                addr = add.lstrip('\r\n\t').rstrip('\r\n\t')
                                address += addr + " "
                        addresses.append(address)
                        cont = v.contents[1].contents[4:]
                        leng = len(cont)

                        for web in cont[:4]:
                            if web.string[:3] == 'www':
                                flag = False
                                websites.append(web.string)
                        if flag:
                            websites.append("Not Found")
        except TypeError as e:
            addresses.append("Not Found")
            websites.append("Not Found")

    print(websites)

    print(addresses)
    #Saving Details

    final_list = []
    for i in range(length):
        dict = {}
        dict['name'] = firm_name[i]
        dict['opportunities'] = job[i]
        dict['url'] = links[i]
        dict['website'] = websites[i]
        dict['address'] = addresses[i]
        final_list.append(dict)
    save(final_list)


except Exception as e:
    print(e)


