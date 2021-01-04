from selenium import webdriver
import time
import json


FILE_NAME = FILE_PATH

def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
page  = 1      #If you want to scrape from 500 then keep it as 501 i.e start_index + 1
links = []
name = []
try:
    while page < 18:  # keep the upper bound here
        url = f'https://www.volunteermatch.org/search/orgs.jsp?l=Argentina&k=&submitsearch=Search' # Enter the url here
        page += 10
        driver.get(url)
        time.sleep(pause_time)
        val = driver.find_elements_by_tag_name('div')
        for v in val:
            if v.get_attribute('id') == 'searchresults':
                link = v.find_elements_by_tag_name('a')
                count = 0
                for i in link:
                    if count == 0:
                        name.append(i.text)
                        links.append(i.get_attribute('href'))
                    count += 1
                    if count == 3:
                        count = 0
except Exception as e:
    print(e)
# print(name)
# print(links)
# print(len(name))
# print(len(links))
driver.quit()
mission_Statement = []
Description = []
focus_areas = []
social_profiles = []
website = []
address = []
donate_link = []
opportunities = []
average_review = []
no_of_review = []
try:
    c = 1
    for i in links :
        print(c)
        c += 1
        driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        driver.get(i)
        time.sleep(pause_time)
        try:
            ul = driver.find_element_by_class_name('causes_icon_display')
            li = ul.find_elements_by_tag_name('li')
            interest = []
            for k in li:
                l = k.find_element_by_tag_name('img')
                # print(l.get_attribute('title'))
                interest.append(l.get_attribute('title'))
                if l.get_attribute('title') == '':
                    exit(0)
            focus_areas.append(interest)
        except Exception as e:
            print(e)
            focus_areas.append("Not Found")
        try:
            don = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[1]/div/section/a')
            # print(don.get_attribute('href'))
            donate_link.append(don.get_attribute('href'))
        except Exception as e:
            print(e)
            donate_link.append("Not Found")
        try:
            opo = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[1]/div/footer/header/h3/span/a')
            # print(opo.text)
            opportunities.append(opo.text)
        except Exception as e:
            print(e)
            opportunities.append("Not Found")
        try:
            rev = driver.find_element_by_class_name('org_review_count')
            # print(type(rev.get_attribute('innerHTML')))
            p = (rev.get_attribute('innerHTML').split('</span>'))
            # print(p[0][-1])
            no_of_review.append(p[0][-1])
        except Exception as e:
            print(e)
            no_of_review.append("No Reviews")
        try:
            star_url = "https://d3bl5qcndhcx94.cloudfront.net/rel206-d314407f/images/full_star.gif"
            empty_star = "https://d3bl5qcndhcx94.cloudfront.net/rel206-d314407f/images/empty_star.gif"
            half_star = "https://d3bl5qcndhcx94.cloudfront.net/rel206-d314407f/images/half_star.gif"
            avg = driver.find_element_by_class_name('count')
            img = avg.find_elements_by_tag_name('img')
            print(img)
            count = 0
            for i in img:
                print(i.get_attribute('src'))
                if "full_star" in  str(i.get_attribute('src')):
                    count += 1
                elif "half_star" in str(i.get_attribute('src')):
                    count += 0.5
            average_review.append(count)
            print(count)
        except Exception as e:
            print(e)
            average_review.append("Not Found")
        try:
            addre = driver.find_element_by_tag_name('address')
            # print(addre.text)
            address.append(addre.text)
        except Exception as e:
            print(e)
            address.append("Not Found")
        button = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[2]/div/ul/li[2]/a')
        button.click()
        try:
            miss = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[2]/div/div/div[2]/div/div/div[1]/section[1]/p')
            # print(miss.text)
            mission_Statement.append(miss.text)
        except Exception as e:
            print(e)
            mission_Statement.append("Not Found")
        try:
            desc = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[2]/div/div/div[2]/div/div/div[1]/section[2]/p')
            # print(desc.text)
            Description.append(desc.text)
        except Exception as e:
            print(e)
            Description.append("Not Found")
        try:
            web = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[2]/div/div/div[2]/div/div/div[2]/section[1]/p/a')
            # print(web.get_attribute('href'))
            website.append(web.get_attribute('href'))
        except Exception as e:
            print(e)
            website.append("Not Found")
        try:
            pro = []
            ul = driver.find_element_by_xpath('/html/body/div[3]/div[2]/main/div/section[2]/div/div/div[2]/div/div/div[2]/section[2]/ul')
            li = ul.find_elements_by_tag_name('li')
            for l in li:
                a = l.find_element_by_tag_name('a')
                # print(a.get_attribute('href'))
                pro.append(a.get_attribute('href'))
            social_profiles.append(pro)
        except Exception as e:
            social_profiles.append("Not Found")
        driver.quit()
    # print(focus_areas)
    # print(mission_Statement)
    # print(social_profiles)
    # print(Description)
    # print(website)
    # print(address)
    # print(donate_link)
    # print(opportunities)
    # print(average_review)
    # print(no_of_review)
except :
    print("error")
length = len(address)
final_list = []
for i in range(length):
    dict = {}
    dict['name'] = name[i]
    dict['link'] = links[i]
    dict['focus_Area'] = focus_areas[i]
    dict['mission_Statement'] = mission_Statement[i]
    dict['Description'] = Description[i]
    dict['website'] = website[i]
    dict['social_profiles'] = social_profiles[i]
    dict['address'] = address[i]
    dict['NoOfOpportunities'] = opportunities[i]
    dict['averagereview'] = average_review[i]
    dict['donate_link'] = donate_link[i]
    dict['no_of_review'] = no_of_review[i]
    final_list.append(dict)
save(final_list)

