from selenium import webdriver
import time
import json
import re

FILE_NAME = 'C:\\Users\\RealMe\\PycharmProjects\\codes\\allforgood.json'
with open(FILE_NAME,'w') as f:
    a = []
    json.dump(a,f)
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)

pause_time = 2
DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.set_window_position(0, 0)
driver.set_window_size(1920, 1080)
url = "https://www.allforgood.org/search?expandFavorites=false&getRemote=true&radiusDropdown=within%2050%20miles"
links = []
names = []
details = []
address = []
driver.get(url)
time.sleep(pause_time + 5)
c = 1
while c <= 670:
    try:
        c += 1
        p = driver.find_element_by_class_name('search-footer')
        load_more = p.find_element_by_tag_name('a')
        # for i in p:
        #     if i.get_attribute('data-ember-action-467') == "467":
        #         load_more = i
        #         break
        load_more.click()
        time.sleep(pause_time + 3)
        print(c)
    except:
        break
a = driver.find_elements_by_class_name('search-card')
for i in a:
    li = i.find_elements_by_tag_name('a')
    for j in li:
        if j.get_attribute('class') == 'pb-link-sm ember-view':
            # print(j.get_attribute('href'))
            links.append(j.get_attribute('href'))
            # print(j.text)
            names.append(j.text)
    try:
        k = i.find_element_by_class_name('description')
        # print(k.text)
        details.append(k.text)
    except:
        details.append("-")
    try:
        f = i.find_elements_by_tag_name('p')
        for j in f:
            if j.get_attribute('class') == 'pb-copy-sm':
                print(j.text)
                address.append(j.text)
    except:
        address.append("-")
# links = ['https://www.allforgood.org/projects/o83nx0Q5', 'https://www.allforgood.org/projects/78eM0q8p', 'https://www.allforgood.org/projects/9kDnK28q', 'https://www.allforgood.org/projects/LQrNwyQr', 'https://www.allforgood.org/projects/GQwlKr85', 'https://www.allforgood.org/projects/0QWB9lk6', 'https://www.allforgood.org/projects/o83R55Q5', 'https://www.allforgood.org/projects/eJEbMrko', 'https://www.allforgood.org/projects/98nnMl83', 'https://www.allforgood.org/projects/0QWBqmk6', 'https://www.allforgood.org/projects/9kDR1n8q', 'https://www.allforgood.org/projects/P8ojOKQq', 'https://www.allforgood.org/projects/a8vjP18z', 'https://www.allforgood.org/projects/98neE0Q3', 'https://www.allforgood.org/projects/9kAEoPkz', 'https://www.allforgood.org/projects/nQPP91QN', 'https://www.allforgood.org/projects/o832G9Q5', 'https://www.allforgood.org/projects/OkbjAbkz', 'https://www.allforgood.org/projects/mQNjpNQz', 'https://www.allforgood.org/projects/0QWjrRk6', 'https://www.allforgood.org/projects/wkxlX1kR', 'https://www.allforgood.org/projects/YkRj5GkN', 'https://www.allforgood.org/projects/9kDna68q', 'https://www.allforgood.org/projects/P8ojArQq', 'https://www.allforgood.org/projects/D84Rb9kl', 'https://www.allforgood.org/projects/78ejAVJp', 'https://www.allforgood.org/projects/GQaBK78O', 'https://www.allforgood.org/projects/28gjA9QR', 'https://www.allforgood.org/projects/xJYBqZkD', 'https://www.allforgood.org/projects/nQPd61QN', 'https://www.allforgood.org/projects/o83RBRQ5', 'https://www.allforgood.org/projects/P8oj0aQq', 'https://www.allforgood.org/projects/wkxjyn8R', 'https://www.allforgood.org/projects/a8vj4Z8z', 'https://www.allforgood.org/projects/9k2nVGkx', 'https://www.allforgood.org/projects/XJZ3NOk3', 'https://www.allforgood.org/projects/GkXjpw8d', 'https://www.allforgood.org/projects/rQ6n6pQw', 'https://www.allforgood.org/projects/eJEjO4ko', 'https://www.allforgood.org/projects/bJ7npV89', 'https://www.allforgood.org/projects/eJEbmrko', 'https://www.allforgood.org/projects/l81A2N8j', 'https://www.allforgood.org/projects/l81nAqJj', 'https://www.allforgood.org/projects/jJzlvLQX', 'https://www.allforgood.org/projects/qJLjpzQB', 'https://www.allforgood.org/projects/Okbow3Qz', 'https://www.allforgood.org/projects/bJ7nb989', 'https://www.allforgood.org/projects/x85RXzJd', 'https://www.allforgood.org/projects/0QWjVOk6', 'https://www.allforgood.org/projects/x85nwzJd', 'https://www.allforgood.org/projects/9kDnjB8q', 'https://www.allforgood.org/projects/qJLjgzQB', 'https://www.allforgood.org/projects/GQwlX385', 'https://www.allforgood.org/projects/o83RNRQ5', 'https://www.allforgood.org/projects/zQGjAek7', 'https://www.allforgood.org/projects/YQpjdoJ4', 'https://www.allforgood.org/projects/o83RgoQ5', 'https://www.allforgood.org/projects/nQPdRBQN', 'https://www.allforgood.org/projects/jQ9RLd8e', 'https://www.allforgood.org/projects/o83Rz5Q5', 'https://www.allforgood.org/projects/eJEbgrko', 'https://www.allforgood.org/projects/RQdjdAJl', 'https://www.allforgood.org/projects/mQNBwYQz', 'https://www.allforgood.org/projects/GkXAEzQd', 'https://www.allforgood.org/projects/jQ9nYY8e', 'https://www.allforgood.org/projects/xJYElNJD', 'https://www.allforgood.org/projects/GQwlwd85', 'https://www.allforgood.org/projects/qJLjY9QB', 'https://www.allforgood.org/projects/GQa4RYkO', 'https://www.allforgood.org/projects/28gvgOQR', 'https://www.allforgood.org/projects/xJYEjlJD', 'https://www.allforgood.org/projects/XJZqmr83', 'https://www.allforgood.org/projects/Bkmj7YQo', 'https://www.allforgood.org/projects/78ejM3Jp', 'https://www.allforgood.org/projects/78ejbaJp', 'https://www.allforgood.org/projects/98nnbj83', 'https://www.allforgood.org/projects/5kVPyL8z', 'https://www.allforgood.org/projects/bJjmBr86', 'https://www.allforgood.org/projects/x85RE2Jd', 'https://www.allforgood.org/projects/eJEbq0ko', 'https://www.allforgood.org/projects/28gvmjQR', 'https://www.allforgood.org/projects/GQa414kO', 'https://www.allforgood.org/projects/xJYEPLJD', 'https://www.allforgood.org/projects/28gvDZQR', 'https://www.allforgood.org/projects/RQdjxGJl', 'https://www.allforgood.org/projects/D84Rnvkl', 'https://www.allforgood.org/projects/6QylnekZ', 'https://www.allforgood.org/projects/P8ojrrQq', 'https://www.allforgood.org/projects/VQqjRZ8y', 'https://www.allforgood.org/projects/GQwoOLQ5', 'https://www.allforgood.org/projects/28gdYVJR', 'https://www.allforgood.org/projects/jQ9V0D8e', 'https://www.allforgood.org/projects/l81wlVkj', 'https://www.allforgood.org/projects/x85RBqJd', 'https://www.allforgood.org/projects/28gvmgQR', 'https://www.allforgood.org/projects/P8oxbaJq', 'https://www.allforgood.org/projects/D84nl1kl', 'https://www.allforgood.org/projects/78eMxR8p', 'https://www.allforgood.org/projects/GQa47pkO', 'https://www.allforgood.org/projects/28gvwVQR', 'https://www.allforgood.org/projects/xJYEyRJD', 'https://www.allforgood.org/projects/nQPjqwJN', 'https://www.allforgood.org/projects/9kAj09Qz', 'https://www.allforgood.org/projects/o83ReAQ5', 'https://www.allforgood.org/projects/R8OLggJM', 'https://www.allforgood.org/projects/jQ9yMyQe', 'https://www.allforgood.org/projects/98n6bX83', 'https://www.allforgood.org/projects/9kAj1GQz', 'https://www.allforgood.org/projects/YkRjY0kN', 'https://www.allforgood.org/projects/bJjmbr86', 'https://www.allforgood.org/projects/RJKjdP8X', 'https://www.allforgood.org/projects/P8ojxyQq', 'https://www.allforgood.org/projects/eJEb5Gko', 'https://www.allforgood.org/projects/x85R3WJd', 'https://www.allforgood.org/projects/eJEbY9ko', 'https://www.allforgood.org/projects/28gvwjQR', 'https://www.allforgood.org/projects/GQa40XkO', 'https://www.allforgood.org/projects/RQd13D8l', 'https://www.allforgood.org/projects/a8vrRX8z', 'https://www.allforgood.org/projects/bJ7naB89', 'https://www.allforgood.org/projects/RJMBxVkP', 'https://www.allforgood.org/projects/a8vrZn8z', 'https://www.allforgood.org/projects/R8ORK1QM', 'https://www.allforgood.org/projects/RJMjKekP', 'https://www.allforgood.org/projects/l81n9bJj', 'https://www.allforgood.org/projects/6QylxlkZ', 'https://www.allforgood.org/projects/OkbooGQz', 'https://www.allforgood.org/projects/eJEjbBko', 'https://www.allforgood.org/projects/28gjvgQR', 'https://www.allforgood.org/projects/YQpjyaJ4', 'https://www.allforgood.org/projects/wkxj758R', 'https://www.allforgood.org/projects/rQ6RVgQw', 'https://www.allforgood.org/projects/9k2RMzkx', 'https://www.allforgood.org/projects/XJZj2VJ3', 'https://www.allforgood.org/projects/bJ7RmB89', 'https://www.allforgood.org/projects/BkmjeVQo', 'https://www.allforgood.org/projects/5kVBVokz', 'https://www.allforgood.org/projects/4Q0Rd0JR', 'https://www.allforgood.org/projects/D84nn3kl', 'https://www.allforgood.org/projects/P8ojvaQq', 'https://www.allforgood.org/projects/GQaBnp8O', 'https://www.allforgood.org/projects/GQa425kO', 'https://www.allforgood.org/projects/YQpprNQ4', 'https://www.allforgood.org/projects/6Qyjln8Z', 'https://www.allforgood.org/projects/GQaB448O', 'https://www.allforgood.org/projects/9kAR14Qz', 'https://www.allforgood.org/projects/dJBRdaJ5', 'https://www.allforgood.org/projects/GQwRqdk5', 'https://www.allforgood.org/projects/78ejBqJp', 'https://www.allforgood.org/projects/x85nmZJd', 'https://www.allforgood.org/projects/jQ906xke', 'https://www.allforgood.org/projects/P8oxxzJq', 'https://www.allforgood.org/projects/GQaAZgQO', 'https://www.allforgood.org/projects/9k2nerkx', 'https://www.allforgood.org/projects/GQa4vjkO', 'https://www.allforgood.org/projects/o83n6GQ5', 'https://www.allforgood.org/projects/9kDnXV8q', 'https://www.allforgood.org/projects/GQa4M4kO', 'https://www.allforgood.org/projects/9kDnVL8q', 'https://www.allforgood.org/projects/dJBRzPJ5', 'https://www.allforgood.org/projects/VQqR3E8y', 'https://www.allforgood.org/projects/Okbj9Rkz', 'https://www.allforgood.org/projects/mQNBxLQz', 'https://www.allforgood.org/projects/GQwRoLk5', 'https://www.allforgood.org/projects/YQpj9zJ4', 'https://www.allforgood.org/projects/rQ6RqAQw', 'https://www.allforgood.org/projects/9k2RjMkx', 'https://www.allforgood.org/projects/XJZje6J3', 'https://www.allforgood.org/projects/R8ORbgQM', 'https://www.allforgood.org/projects/RJMBpwkP', 'https://www.allforgood.org/projects/dJBjKPJ5', 'https://www.allforgood.org/projects/rQ6neKQw', 'https://www.allforgood.org/projects/78eMdn8p', 'https://www.allforgood.org/projects/l81nLNJj', 'https://www.allforgood.org/projects/9kAj2KQz', 'https://www.allforgood.org/projects/YkRjEMkN', 'https://www.allforgood.org/projects/o83n3aQ5', 'https://www.allforgood.org/projects/eJEjZZko', 'https://www.allforgood.org/projects/l81n5DJj', 'https://www.allforgood.org/projects/6Qyl5nkZ', 'https://www.allforgood.org/projects/P8oxNyJq', 'https://www.allforgood.org/projects/D84n9vkl', 'https://www.allforgood.org/projects/78eM038p', 'https://www.allforgood.org/projects/YQppzrQ4', 'https://www.allforgood.org/projects/wkxlRMkR', 'https://www.allforgood.org/projects/rQ6nW2Qw', 'https://www.allforgood.org/projects/D84noOkl', 'https://www.allforgood.org/projects/78eMnz8p', 'https://www.allforgood.org/projects/GQa4qAkO', 'https://www.allforgood.org/projects/qJLjODQB', 'https://www.allforgood.org/projects/GQwlWY85', 'https://www.allforgood.org/projects/x85nYqJd', 'https://www.allforgood.org/projects/1JlZWYQz', 'https://www.allforgood.org/projects/GQwygdJ5', 'https://www.allforgood.org/projects/4Q0RMgJR', 'https://www.allforgood.org/projects/D84nPBkl', 'https://www.allforgood.org/projects/78eM1q8p', 'https://www.allforgood.org/projects/a8vjvY8z', 'https://www.allforgood.org/projects/jQ9VRp8e', 'https://www.allforgood.org/projects/78ejOWJp', 'https://www.allforgood.org/projects/RQdBZgJl', 'https://www.allforgood.org/projects/XJZ9zV83', 'https://www.allforgood.org/projects/9kARd2Qz', 'https://www.allforgood.org/projects/VQqjvE8y', 'https://www.allforgood.org/projects/o83RgGQ5', 'https://www.allforgood.org/projects/D841vxJl', 'https://www.allforgood.org/projects/zQGGL1Q7', 'https://www.allforgood.org/projects/jQ9OYDJe', 'https://www.allforgood.org/projects/rQ6n5KQw', 'https://www.allforgood.org/projects/1JlZ2jQz', 'https://www.allforgood.org/projects/wkxz4l8R', 'https://www.allforgood.org/projects/o83YeKk5', 'https://www.allforgood.org/projects/YkRBVLkN', 'https://www.allforgood.org/projects/0QWB6ok6', 'https://www.allforgood.org/projects/P8oaxakq', 'https://www.allforgood.org/projects/YkRjrrkN', 'https://www.allforgood.org/projects/78eYMz8p', 'https://www.allforgood.org/projects/qJLDBzJB', 'https://www.allforgood.org/projects/dJBjZaJ5', 'https://www.allforgood.org/projects/78ej1VJp', 'https://www.allforgood.org/projects/D84yD1Jl', 'https://www.allforgood.org/projects/GkXypjQd', 'https://www.allforgood.org/projects/RQdNw0Jl', 'https://www.allforgood.org/projects/jQ93ENJe', 'https://www.allforgood.org/projects/98nPYBk3', 'https://www.allforgood.org/projects/1JlZzXQz', 'https://www.allforgood.org/projects/mQNmRAkz', 'https://www.allforgood.org/projects/l81V0rJj', 'https://www.allforgood.org/projects/6QylzxkZ', 'https://www.allforgood.org/projects/P8oxenJq', 'https://www.allforgood.org/projects/nQPdnVQN', 'https://www.allforgood.org/projects/VQq4xEky', 'https://www.allforgood.org/projects/GQwY99J5', 'https://www.allforgood.org/projects/Bkm2Z1Qo', 'https://www.allforgood.org/projects/D84Rl6kl', 'https://www.allforgood.org/projects/zQGj6Yk7', 'https://www.allforgood.org/projects/jJzlEaQX', 'https://www.allforgood.org/projects/jJzlMvQX', 'https://www.allforgood.org/projects/9kARmRQz', 'https://www.allforgood.org/projects/RJKjYX8X', 'https://www.allforgood.org/projects/LQrNAdQr', 'https://www.allforgood.org/projects/jJzlxMQX', 'https://www.allforgood.org/projects/78eMea8p', 'https://www.allforgood.org/projects/RJMjWzkP', 'https://www.allforgood.org/projects/zQG2l6k7', 'https://www.allforgood.org/projects/P8o3Gy8q', 'https://www.allforgood.org/projects/OkbKPGQz', 'https://www.allforgood.org/projects/bJ7nxl89', 'https://www.allforgood.org/projects/9kA5O4kz', 'https://www.allforgood.org/projects/bJjBNAJ6', 'https://www.allforgood.org/projects/1JlBmXQz', 'https://www.allforgood.org/projects/eJEjx4ko', 'https://www.allforgood.org/projects/jQ95DDQe', 'https://www.allforgood.org/projects/1JlEzOkz', 'https://www.allforgood.org/projects/jQ9O2YJe']
# names = ['Write a Concept Note on Equal Rights to Women and Prevention of Violence against women', 'Indian website famous for all fun and exciting 1000+ games.', 'Internships Opportunities at Maple Leaf Hospital Facility', 'Tutors for Project EDvantage', 'Social Travel in South India', 'Longest Human Chain', 'Secretary for Project EDvantage', 'Executive Board for Project EDvantage', 'Executive Board For Cards.In.Kindness.Mumbai', 'Virtual Cards', 'Children & youth education', 'Project EDvantage Volunteers', 'Education for free - Need tech developers', 'Teaching & Assisting in Schools in Rural Areas', 'Women’s Empowerment & Rights', 'Teaching English to underprivileged students', 'DIVERSIFIED VOLUNTEER GROUP', 'A crowd-guided Applied Research Project on Indian Parenting Habits.', 'Volunteer in Rajasthan', 'Video Editor', 'Volunteer in Mumbai', 'Prepare video based courses of Science', 'Buy a $3 (USD) book and get 50 Volunteer hours!', 'Write Poems for The Teen Pop', 'Write Short Stories for The Teen Pop', 'Write DIY articles for The Teen Pop', 'Write Lifestyle articles for The Teen Pop', 'Write Celebrity articles for The Teen Pop', 'Write Wellness articles for The Teen Pop', 'Write Activism articles for The Teen Pop', 'Write Beauty articles for The Teen Pop', 'Be our Social Media Manager!', 'Writing Magazine Articles for The Teen Pop', 'Write for us!', 'Volunteer in New Delhi', 'Social Travel in North India', 'Volunteer in Varanasi', 'Volunteer in Rishikesh', 'Adding and Promotion of Google ads and conversion tracking tags to our WordPress website', 'Life in a Pahadi Village', 'Virtual Online Volunteering Opportunities in Nepal', 'Public Health and Sanitation Internship in Himalayas', 'FEED THE STREETS OF NEPAL', 'Volunteer in Mysore', 'Training Curriculum Development', 'Graphic Design Support', 'School on street in City of Joy Teach basic English to the poor children.', 'Principal To Start A School for Underprivileged', 'Street Children welfare', 'Stray dogs welfare', 'Yoga and meditation workshop', 'Rooftop Organic farming', 'Word press (Web design wizardry)', 'Education and action project for children and women development', 'Volunteer in Kochi', 'Course Assistant', 'Officer of Social Media Management', 'Specialist of IT', 'Specialist in Public Speaking', 'Officer of Workshop Management', 'Officer of Volunteer Management', 'Specialist of English', 'Specialist in Arduino Programming & building', 'Specialist in Animation Making', 'High School Students: Join our mental health chapter in Sharjah, UAE', 'STEM OR COMMERCE BACKGROUND TUTOR/COMMUNITY OUTREACH/SOCIAL MEDIA/SCIENCE BLOGGER/ RESEARCHER', 'Outreach and Magazine/Web Design Leaders', 'Healthcare Workers Appreciation Letter Writing Initiative', 'Dream Big Bahrain', 'Dream Big', 'Scholars of Sustenance: Volunteer Program (VoPro)', 'Volunteers are required to design modern website pages. The site is made up of three main', 'Volunteers are Vital: See the countryside, Meet the people and See the impact we are making', 'Medan Volun-tourist (Traveler Volunteer)', 'At-Home Guardian Angel Volunteers Make a Meaningful Impact from the Comfort of Your Own Home', 'Medan Volun-tourist (Traveler Volunteer)', 'Voluntourist (Traveler Volunteer) - Medan', 'Explore the South of Vietnam while helping us to teach English for Kids', 'Volunteer to Empower Women', 'Designer to create our speaker brochure and promotional flyer for our USA chapter', 'Befriending Special Persons', 'Emmanuel Second Chance Education Programme (ESCEP) Career Mentor', 'Medical Escorts', 'I am a Genuine Egyptian', 'Jakarta Volun-tourist (Traveler Volunteer)', 'Jakarta Volun-tourist (Traveler Volunteer)', 'Adopt a sheltered, stray, or rescued animal today!', 'At-Home Webmaster and IT Volunteer', 'At-Home Webmaster and IT Volunteer', 'Graphic Designer Needed Make a Meaningful Impact from the Comfort of Your Own Home', 'Volunteer with IHF Kenya Famine Relief and Education Programs', 'Watamu Sea Turtle Volunteer Project, Kenya', 'Adolescent Sexual reproductive health', 'Create Cheap artificial reef', 'Help Us Save the Antipolo City Pound Dogs from Inhumane Mass Euthanasia', 'Sign up for our Writing Department!', 'Sign up for our Public Relations Department!', 'Sign up for our Marketing Department!', 'Sign up for our Logistics Department!', 'Sign up for our Graphic Design Department!', 'Sign up for our Animal Adoption Department!', 'Senior Recruiter/HR manager', 'Senior full-stack engineer', 'Infectious Disease Prevention', 'At Home Translator', 'Community Work', 'Technical Support Office, Fluent in English, Previous Tech & NGO Admin Experience', 'Experienced Interpreters for French, Arabic, Farsi (Remote & Greece)', 'Greece Appeals Team, Fluent in English, Previous Appeals Drafting Experience (remote or Greece)', 'Mental Health & Psychosocial Services (MHPSS) Team Service Provider (field)', 'Legal Field Team, Fluent in English, Qualified Lawyer', 'Kenya Volun-tourist (Traveler Volunteer)', 'Kenya Volun-tourist (Traveler Volunteer)', 'Kenyan Legal Consultant Volunteer Make a Meaningful Impact from the Comfort of Your Own Home', 'volunteer for better community', 'Volunteering Tanzania Africa', 'Program Assistant', 'Promoting Access to Integrated Community Child Rights Support in Northern Uganda.', 'igniting growth with young entrepreneurs', 'SUPPORT VULNERABLE CHILDREN IN OUR DAYCARE', 'The Green House Project', 'Train and Equip worship leaders in Uganda', 'Train and Equip worship leaders in Uganda', 'Train and Equip worship leaders in Uganda', 'Train and Equip worship leaders in Uganda', 'Train and Equip worship leaders in Uganda', 'Community Outreach volunteers!', 'Social or fun-loving volunteer needed to Volunteer with us!', 'Conservation Volunteering Project Uganda', 'Sports Volunteering Project Uganda', 'Organic Farming Volunteering Project Uganda', 'Teaching Volunteering Project Uganda', 'Childcare Volunteering Project Uganda', 'Women Empowerment Volunteering Project Uganda', 'Construction and Building Volunteering Project Uganda', 'Community Development Volunteering Uganda', 'Arts and Music Volunteering Project Uganda', 'Medical and Healthcare Volunteering Project Uganda', 'German friendship organization/club', 'Youth Breakthrough Program Volunteer', 'Coach - Deaf Volleyball Team', 'Teaching extra curriculum studies: Arts, Music, Sports & Games', "GIRL'S SAFETY AND EDUCATION PROJECT", 'At-Home Teacher Training Volunteer', 'Bali Voluntourist Traveler Volunteer', 'Bali Voluntourist Traveler Volunteer', 'At-Home Media and Public Relations Volunteer', 'At-Home Finance Volunteer', 'Website Manager', 'I need a person to help me with my social media account', 'VOLUNTEER OPPORTUNITIES IN RWANDA', "Volunteer teachers where are you? You don't need to be a qualified or experienced.", 'Revolutionizing The Female Gender For Africa', 'Community education project near lake malawi', 'Support education of girls in Minembwe, DR Congo', 'Fighting against child marriage in FIZI Territory / Democratic republic of Congo', "Uceio dell'Aquila", 'Looking for a host to our youtube channel', 'Call for champions and members', 'Marine Conservation Field Experience, Mozambique', 'Community Teaching and Development', 'We need Academic Volunteers in our College of Medical Sciences at HIPDET University in Cameroon', 'We need Academic Volunteers in our College of Agriculture at HIPDET University in Cameroon', 'We need Academic Volunteers in our College of Law at HIPDET University in Cameroon', 'We need Academic Volunteers in our College of Arts, Social Sciences, and Humanities at HIPDET U.', 'We need Academic Volunteers in our College of Education at HIPDET University in Cameroon', 'We need Academic Volunteers in our College of Business & Technology at HIPDET University in Cameroon', 'We need technical advisors and non - academic Volunteers in our College of Vocational Training', 'Sending Support to Seniors Project (only through virtual means)', 'Tree-Nation Online Volunteer', 'Volunteers wanted at the College for International Co-operation and Development!', 'Help Save Lewisham Community Transport Scheme', 'Digital marketing roles: - Email marketing - Social media - Web content - PR - Digital advertising', 'Amstadd Effective altruism', 'IT Administrator (Volunteer- Unpaid)', 'Finance Manager (Volunteer- Unpaid)', 'EA/PA (Internship - Unpaid)', 'Volunteer Mentor (Volunteer- Unpaid)', 'Lecture (Volunteer- Unpaid)', 'Entrepreneur Mentor (Volunteer- Unpaid)', 'Software Developer (Volunteer- Unpaid)', 'Content Coordinator (Volunteer- Unpaid)', 'CH Associate (Volunteer- Unpaid)', 'Grant Writer (Volunteer- Unpaid)', 'Writer (Volunteer- Unpaid)', 'Counselling Supervisor (Volunteer- Unpaid)', 'Internal Communication Manager (Volunteer- Unpaid)', 'Mentor Team Leader (Volunteer- Unpaid)', 'Online Course Content Coordinator (Volunteer- Unpaid)', 'Charity Fundraiser (Volunteer- Unpaid)', 'Business Development Manager (Volunteer- Unpaid)', 'Buy a $3 (USD) book and get 50 Volunteer hours!', 'Giant Health 2020', 'Changemakers', 'Alinah vulnerable community helper none profit organisation', 'Wellfield Wellfare', 'Wellfield Wellfare', 'Support Worker working with vulnerable young adults aged 16-25', 'Volunteer at the Jane Goodall Chimpanzee Sanctuary in South Africa', 'Free Online Education for teens and young adult:This involves content development on various topics.', 'Free Medical Services', 'Write online course in Agriculture', 'Volunteer Mentor', 'We need Academic and Non-Academic Volunteers at HIPDET University in Cameroon', 'Website Development & Updating', 'Women Empowerment Center: Addressing the needs of youths located in remote communities', 'YOUTH COMMUNITY TRAINING FOR SELF-EMPLOYMENT', 'FUNDRAISING & RESOURCE MOBILIZATION VOLUNTEERS', 'FINANCIAL OPERATIONS FOR NON-PROFIT', 'Building of bore holes for good drinkable water and rural electrification in my community', 'IT & Communication', 'Improving the teaching and learning activities of Orphans and Vulnerable Children in Slum Community', 'An anti-corruption Christian initiative that stir believers in Nigeria to help control corruption', 'Writing Articles', 'TILDACARE YULETIDE OUTREACH', 'BP100: Make Bohicon the cleanest city in Benin by 2025', 'Give your language a way to your Host', 'Web Developing and design', 'Families', 'Long-term Volunteers Needed for Managing Content on Our Social Media Accounts', 'Conservation Volunteers Australia & New Zealand', 'Volunteering Opportunities in Ghana.', 'COMMUNITY DEVELOPMENT', 'Poor and Needy Outreach..', 'Help in our charity school,help disable children and other social projects.', 'Volunteer as a tutor . Volunteer as a health official', 'Nationwide Educational Support Tour', 'African Fashion wear Project', 'HOUSING AND SHELTER', 'HOUSING AND SHELTER', 'MSCF VOLUNTEER PROGRAM', '1.orphanage care 2. street care project 3. teaching 4. sports coaching 5. Journalism 6. law', 'VOLUNTEER YOUR TIME', 'Use your professional skill for good', 'Senior Chef', 'Answering calls remotely', 'Answering calls remotely', 'Volunteers Needed to Support Response to COVID Second Wave', 'Make Cards and Letters for Seniors // EARN VOLUNTEER HOURS', 'Students Teach Students - boostskills.org', 'Advocate', 'Covid-19 Data/Interview collection', 'Volunteer Outreach/opportunities research and Website Design', 'French Tutor', 'Help out at a small animal shelter', 'Volunteers needed to help out in store. Repairing furniture, stocking the floor and running things.', 'Camp Retreat Volunteers', 'Have you experienced poverty? Raise your voice as an advocate.', 'American Red Cross - Development Support!', 'American Red Cross - Virtual Volunteer Scheduler!', 'American Red Cross - Help At Blood Drives!', 'Food Distribution/Community Volunteer', 'American Red Cross - Help Recruit Volunteers!', 'Help families struggling with basic needs', 'Second Life Thrift Store Proceeds go to local Animal Rescue']
print(links)
print(names)
print(len(links))
print(len(names))
organisation = []
org_link = []
email = []
impact_area = []
mobile = []
count = 0
for i in links:
    print(count + 1)
    print(i)
    driver.get(i)
    time.sleep(3)
    flg = False
    try:
        a = driver.find_element_by_class_name("pb-link")
        print(a.text)
        organisation.append(a.text)
        org_link.append(a.get_attribute('href'))
    except:
        org_link.append("-")
        organisation.append("-")
    try:
        flg = True
        a = driver.find_elements_by_tag_name('article')
        for j in a:
            if j.get_attribute('class') == "show-contact-info":
                k = str(j.text).split("\n")
                l = re.findall('\S+@\S+', j.text)
                print(l)
                if len(l) == 0:
                    email.append("-")
                else:
                    email.append(l)
                mflag = False
                for i in k:
                    if i.isnumeric():
                        print(i)
                        mobile.append(i)
                        mflag = True
                        break
                if not mflag:
                    mobile.append("-")
    except:
        print("Null")
        email.append("-")
        mobile.append("-")
    try:
        a = driver.find_elements_by_tag_name('section')
        for j in a:
            if j.get_attribute('class') == "service-box":
                l = str(j.text).split("\n")
                l = l[1:]
                print(l)
                if len(l) == 0:
                    impact_area.append("-")
                else:
                    impact_area.append(l)
    except:
        print("NULL")
        impact_area.append("-")
    if len(email) - 1 < count:
        email.append("-")
    if len(mobile) - 1 < count:
        mobile.append("-")
    if len(org_link) - 1 < count:
        org_link.append("-")
    if len(organisation) - 1< count:
        organisation.append("-")
    if len(impact_area) - 1< count:
        impact_area.append("-")
    with open(FILE_NAME) as file:
        data = json.load(file)
    va = {}
    try:
        va['name'] = names[count]
        va['link'] = links[count]
        va['organisation'] = organisation[count]
        va['org_link'] = org_link[count]
        va['email'] = email[count]
        va['impact_areas'] = impact_area[count]
        va['phone'] = mobile[count]
        va['details'] = details[count]
        va['address'] = address[count]
        data.append(va)
        save(data)
        count += 1
    except:
        print(count)