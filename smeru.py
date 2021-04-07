import json
FILE_NAME = filename
def save(x):
    with open(FILE_NAME,'w') as f:
        json.dump(x,f)
file = open('edit.txt',encoding='utf-8')
values= file.readline()
val = values.split('\t')
print(val)
length = len(val)
print(length)
num = 2
for i in range(1,length):

    val[i] = val[i].strip(str(num))
    num += 1

print(val)
phoneNo = []
name = []
email = []
web = []
for i in range(1,length):
    p = val[i]
    a,b,c,d = '','','',''
    a = p
    if 'Ph.' in p:
        try:
            a,b = p.split('Ph.')
        except:
            print("error")
    else:
        b = a
    if 'Email' in b:
        try:
            b,c = b.split('Email')
        except:
            print("error")
    else:
        c = b
    if 'Web' in c:
        try:
            c,d = c.split('Web')
        except:
            print("error")
    name.append(a)
    if b == '':
        phoneNo.append("Not Found")
    else:
        phoneNo.append(b)
    if c == '':
        email.append("Not Found")
    else:
        email.append(c)
    if d == '':
        web.append("Not Found")
    else:
        web.append(c)
print(email)
print(phoneNo)
print(name)
print(web)
print(len(web))
print(len(email))
print(len(name))
print(len(phoneNo))
length = len(name)
final_li = []
for i in range(length):
    email[i] = email[i].strip(':')
print(email)
for i in range(length):
    val = {}
    val['Name'] = name[i]
    val['PhoneNo.'] = phoneNo[i]
    val['email'] = email[i]
    val['Web'] = web[i]
    final_li.append(val)
save(final_li)
